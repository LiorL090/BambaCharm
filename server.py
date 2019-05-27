import socket
import select
import sqlite3
import re
import os
import shutil
import pickle
import hashlib
import secrets
import nacl.utils
from nacl.public import PrivateKey, Box

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 8820))
server_socket.listen(5)
open_client_sockets = []
messages_to_send = []
logged_users = {}
encryption_boxes = {}
clients_uploading_file = {}
db = sqlite3.connect('users')
cursor = db.cursor()


class ClientSocket:
    def __init__(self, user_name, user_socket):
        self.user_name = user_name
        self.socket = user_socket
        self.receiving_file = False
        self.file_data = b''
        self.file_path = ''


def hash_password(salt, password):
    """ Hashes password with salt for security reasons"""
    string = salt + password
    hashed_password = hashlib.sha256(string.encode()).hexdigest()
    return hashed_password


def new_salt():
    """ Generates new secure-random salt"""
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    salt = ''.join(secrets.choice(alphabet) for i in range(16))
    return salt


def old_user(this_socket, message):
    """ logging old users (user authentication) """
    message = message.split(" ")
    if len(message) == 3 and '' not in message:
        user_name = message[1]
        password = message[2]

        if len(user_name) <= 15:
            cursor.execute('''SELECT * FROM users WHERE name=?''', (user_name,))
            data = cursor.fetchone()

            if data is None:
                messages_to_send.append((this_socket, "Couldn't find your BambaCharm Account"))
            else:
                # hashes given password using users salt
                salt = data[3]
                hashed_password = hash_password(salt, password)
                if data[1] == hashed_password:
                    messages_to_send.append((this_socket, "successful login"))
                    client = ClientSocket(user_name, this_socket)
                    logged_users[this_socket] = client
                else:
                    messages_to_send.append((this_socket, "wrong password"))
        else:
            messages_to_send.append((this_socket, "Couldn't find your BambaCharm Account"))
    else:
        messages_to_send.append((this_socket, "wrong username or password"))


def new_user(this_socket, message):
    """ creating account for new users (user registration)"""

    message = message.split(" ")
    if len(message) == 4 and '' not in message:
        user_name = message[1]
        password = message[2]
        # Create salt and hashes password
        salt = new_salt()
        hashed_password = hash_password(salt, password)

        if len(user_name) <= 15:
            cursor.execute('''SELECT name  FROM users WHERE name=?''', (user_name,))
            data = cursor.fetchone()
            if data is None:
                email = message[3]
                match = re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email)
                if match:
                    email = match.group()  # 'alice-b@google.com'

                    cursor.execute('''INSERT INTO users(name, password, email, salt)
                                      VALUES(?,?,?,?)''', (user_name, hashed_password, email, salt))
                    db.commit()

                    messages_to_send.append((this_socket, "successful registration"))
                    client = ClientSocket(user_name, this_socket)
                    logged_users[this_socket] = client
                    os.mkdir("storage/%s" % user_name)

                else:
                    messages_to_send.append((this_socket, "wrong email"))
            else:
                messages_to_send.append((this_socket, "username already exist"))
        else:
            messages_to_send.append((this_socket, "user_name should be no longer than 15 symbols"))
    else:
        messages_to_send.append((this_socket, "wrong username or password"))


def handle_client(this_socket, message):
    """handles client requests"""
    message = message.split(" ")
    name = logged_users[this_socket].user_name
    if 1 < len(message):
        if message[1] == "logout":
            logged_users.pop(this_socket)

        # deletes users account
        if message[1] == "delete":
            cursor.execute('''SELECT name  FROM users WHERE name=?''', (name,))
            data = cursor.fetchone()
            if data is not None:
                logged_users.pop(this_socket)
                cursor.execute('''DELETE FROM users
                WHERE name = "%s";
                 ''' % name)
                db.commit()
                shutil.rmtree("storage/%s" % name)

        # sends list of all files in users directory
        if message[1] == "listDir":
            files_list = os.listdir("storage/%s" % name)
            data = pickle.dumps(files_list)
            messages_to_send.append((this_socket, data))

        # deletes the file_data from users directory
        if message[1] == "deleteFile":
            file_name = ' '.join(map(str, message[2:]))
            file_path = "storage/" + name + "/" + file_name
            if file_name:
                if os.path.exists(file_path):
                    os.remove(file_path)

        # sends the file_data to the user
        if message[1] == "giveFile":
            file_name = ' '.join(map(str, message[2:]))
            file_path = "storage/" + name + "/" + file_name
            if file_name:
                if os.path.exists(file_path):
                    file = open(file_path, 'r').read()
                    messages_to_send.append((this_socket, file))

        # saves the file_data that user want to upload
        if message[1] == "uploadFile":
            file_name = ' '.join(map(str, message[2:]))
            file_path = "storage/" + name + "/" + file_name
            if file_name:
                logged_users[this_socket].file_path = file_path
                logged_users[current_socket].receiving_file = True
                messages_to_send.append((this_socket, "ready"))


def send_waiting_messages(wlist):
    try:
        for message in messages_to_send:
            (client_socket, data) = message
            if client_socket in wlist:
                if isinstance(data, str):
                    data = data.encode('utf-8')
                box = encryption_boxes[client_socket]
                encrypted_data = box.encrypt(data)
                client_socket.sendall(encrypted_data)
                messages_to_send.remove(message)
    except:
        pass


while True:
    try:
        rlist, wlist, xlist = select.select([server_socket] + open_client_sockets, open_client_sockets, [])
        for current_socket in rlist:
            if current_socket is server_socket:
                (new_socket, address) = server_socket.accept()
                open_client_sockets.append(new_socket)
            else:
                try:
                    recv_data = current_socket.recv(4096)
                    # if the socket doesnt have secure encryption we create it for him
                    if current_socket not in encryption_boxes.keys():
                        sk_server = PrivateKey.generate()
                        pk_server = sk_server.public_key
                        pk_client = pickle.loads(recv_data)
                        server_box = Box(sk_server, pk_client)
                        encryption_boxes[current_socket] = server_box
                        current_socket.sendall(pickle.dumps(pk_server))

                    # if the socket is sending file to us we accept it until its complete and can be decrypted
                    elif current_socket in logged_users and logged_users[current_socket].receiving_file:
                        logged_users[current_socket].file_data += recv_data
                        try:
                            server_box = encryption_boxes[current_socket]
                            file_data = logged_users[current_socket].file_data
                            file_text = server_box.decrypt(file_data).decode('utf-8')
                            file = open(logged_users[current_socket].file_path, 'w')
                            file.write(file_text)
                            file.close()
                            logged_users[current_socket].receiving_file = False

                        except:
                            pass

                    # basic client requests handler
                    else:
                        server_box = encryption_boxes[current_socket]
                        plaintext = server_box.decrypt(recv_data)
                        recv_message = plaintext.decode('utf-8')
                        if recv_message.startswith("old_user"):
                            old_user(current_socket, recv_message)
                        elif recv_message.startswith("new_user"):
                            new_user(current_socket, recv_message)
                        elif current_socket in logged_users and recv_message.startswith("req"):
                            handle_client(current_socket, recv_message)
                except:
                    pass
        send_waiting_messages(wlist)
    except:
        pass
