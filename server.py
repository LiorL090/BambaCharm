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
    match = re.search(r'old_user ([\w.-]+) ([\w.-]+)', mesage)
    if match:
        user_name = match.group(1)
        password = match.group(2)

        print(user_name + " " + password)

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


def new_user(current_socket, mesage):
    """ creating account for new users (user registration)"""

    match = re.search(r'([\w.-]+)@([\w.-]+)', mesage)
    if match:
        user_name = match.group(1)
        password = match.group(2)

        db = sqlite3.connect('users')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO users(name, password)
                          VALUES(?,?)''', (user_name, password))
        db.commit()


def handle_client(current_socket, mesage):
    """handles client requests"""


def send_waiting_messages(wlist):
    for message in messages_to_send:
        (client_socket, data) = message
        if client_socket in wlist:
            client_socket.send(data.encode('utf-8'))
            messages_to_send.remove(message)


while True:
    rlist, wlist, xlist = select.select([server_socket] + open_client_sockets, open_client_sockets, [])
    for current_socket in rlist:
        if current_socket is server_socket:
            (new_socket, address) = server_socket.accept()
            open_client_sockets.append(new_socket)
        else:
            try:
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
            except:
                pass
    send_waiting_messages(wlist)
