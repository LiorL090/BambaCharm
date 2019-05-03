import socket
import select
import sqlite3
import re

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 8820))
server_socket.listen(5)
open_client_sockets = []
messages_to_send = []
logged_users = {}


class Client_socket():
    def __init__(self, user_name, socket):
        self.user_name = user_name
        self.socket = socket


def old_user(current_socket, mesage):
    """ logging old users (user authentication) """
    mesage = mesage.split(" ")
    if len(mesage) == 3:
        user_name = mesage[1]
        password = mesage[2]

        if len(user_name) <= 15:
            db = sqlite3.connect('users')
            cursor = db.cursor()
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


def new_user(current_socket, mesage):
    """ creating account for new users (user registration)"""

    mesage = mesage.split(" ")
    if len(mesage) == 3:
        user_name = mesage[1]
        password = mesage[2]
        if len(user_name) <= 15:
            db = sqlite3.connect('users')
            cursor = db.cursor()
            cursor.execute('''SELECT name  FROM users WHERE name=?''', (user_name,))
            data = cursor.fetchone()
            if data is None:
                email = mesage[3]
                match = re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email)
                if match:
                    email = match.group()  ## 'alice-b@google.com'

                    cursor.execute('''INSERT INTO users(name, password, email)
                                      VALUES(?,?)''', (user_name, password, email))
                    db.commit()

                    messages_to_send.append((current_socket, "successful registration"))
                    client = Client_socket(user_name, current_socket)
                    logged_users[current_socket] = client

                else:
                    messages_to_send.append((current_socket, "wrong email"))
            else:
                messages_to_send.append((current_socket, "username already exist"))
        else:
            messages_to_send.append((current_socket, "Password should be no longer than 15 symbols"))
    else:
        messages_to_send.append((current_socket, "wrong username or password"))


def handle_client(current_socket, mesage):
    """handles client requests"""
    pass


def send_waiting_messages(wlist):
    for message in messages_to_send:
        (client_socket, data) = message
        if client_socket in wlist:
            client_socket.send(data.encode('utf-8'))
            messages_to_send.remove(message)


while True:
    try:
        rlist, wlist, xlist = select.select([server_socket] + open_client_sockets, open_client_sockets, [])
        for current_socket in rlist:
            if current_socket is server_socket:
                (new_socket, address) = server_socket.accept()
                open_client_sockets.append(new_socket)
            else:

                data = current_socket.recv(1024)
                mesage = data.decode('utf-8')
                if mesage.startswith("old_user"):
                    old_user(current_socket, mesage)
                elif mesage.startswith("new_user"):
                    new_user(current_socket, mesage)
                elif current_socket in logged_users and mesage.startswith("req"):
                    handle_client(current_socket, mesage)
                else:
                    open_client_sockets.remove(current_socket)
        send_waiting_messages(wlist)
    except:
        pass
