import socket
import select
import sqlite3
import re
import os
import shutil
import pickle

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 8820))
server_socket.listen(5)
open_client_sockets = []
messages_to_send = []
logged_users = {}
db = sqlite3.connect('users')
cursor = db.cursor()


class Client_socket():
    def __init__(self, user_name, socket):
        self.user_name = user_name
        self.socket = socket


def old_user(current_socket, message):
    """ logging old users (user authentication) """
    message = message.split(" ")
    if len(message) == 3 and '' not in message:
        user_name = message[1]
        password = message[2]

        if len(user_name) <= 15:
            cursor.execute('''SELECT name, password FROM users WHERE name=?''', (user_name,))
            data = cursor.fetchone()
            if data is None:
                messages_to_send.append((current_socket, "Couldn't find your BambaCharm Account"))
            elif data[1] == password:
                messages_to_send.append((current_socket, "successful login"))
                client = Client_socket(user_name, current_socket)
                logged_users[current_socket] = client
            else:
                messages_to_send.append((current_socket, "wrong password"))
        else:
            messages_to_send.append((current_socket, "Couldn't find your BambaCharm Account"))
    else:
        messages_to_send.append((current_socket, "wrong username or password"))


def new_user(current_socket, message):
    """ creating account for new users (user registration)"""

    message = message.split(" ")
    if len(message) == 4 and '' not in message:
        user_name = message[1]
        password = message[2]
        if len(user_name) <= 15:
            cursor.execute('''SELECT name  FROM users WHERE name=?''', (user_name,))
            data = cursor.fetchone()
            if data is None:
                email = message[3]
                match = re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email)
                if match:
                    email = match.group()  ## 'alice-b@google.com'

                    cursor.execute('''INSERT INTO users(name, password, email)
                                      VALUES(?,?,?)''', (user_name, password, email))
                    db.commit()

                    messages_to_send.append((current_socket, "successful registration"))
                    client = Client_socket(user_name, current_socket)
                    logged_users[current_socket] = client
                    os.mkdir("storage/%s" % user_name)

                else:
                    messages_to_send.append((current_socket, "wrong email"))
            else:
                messages_to_send.append((current_socket, "username already exist"))
        else:
            messages_to_send.append((current_socket, "user_name should be no longer than 15 symbols"))
    else:
        messages_to_send.append((current_socket, "wrong username or password"))


def handle_client(current_socket, message):
    """handles client requests"""
    message = message.split(" ")
    name = logged_users[current_socket].user_name
    if 1 < len(message):
        if message[1] == "logout":
            logged_users.pop(current_socket)

        if message[1] == "delete":
            cursor.execute('''SELECT name  FROM users WHERE name=?''', (name,))
            data = cursor.fetchone()
            if data is not None:
                logged_users.pop(current_socket)
                cursor.execute('''DELETE FROM users
                WHERE name = "%s";
                 ''' % name)
                db.commit()
                shutil.rmtree("storage/%s" % name)

        if message[1] == "listDir":
            list = os.listdir("storage/%s" % name)
            data = pickle.dumps(list)
            messages_to_send.append((current_socket, data))

        if message[1] == "deleteFile":
            file_name = ' '.join(map(str, message[2:]))
            file_path = "storage/" + name + "/" + file_name
            if len(file_name) != 0:
                if os.path.exists(file_path):
                    os.remove(file_path)

        if message[1] == "giveFile":
            file_path = "storage/" + name + "/" + message[2:]
            print(file_path)
            if file_path:
                print(file_path)
                if os.path.exists(file_path):
                    print(file_path)
                    shutil.rmtree(file_path)


def send_waiting_messages(wlist):
    try:
        for message in messages_to_send:
            (client_socket, data) = message
            if client_socket in wlist:
                if isinstance(data, str):
                    data = data.encode('utf-8')
                client_socket.sendall(data)
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
                    data = current_socket.recv(1024)
                    message = data.decode('utf-8')
                    if message.startswith("old_user"):
                        old_user(current_socket, message)
                    elif message.startswith("new_user"):
                        new_user(current_socket, message)
                    elif current_socket in logged_users.keys() and message.startswith("req"):
                        handle_client(current_socket, message)
                    else:
                        open_client_sockets.remove(current_socket)
                except:
                    open_client_sockets.remove(current_socket)
        send_waiting_messages(wlist)
    except:
        pass
