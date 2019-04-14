import socket

my_socket = socket.socket()
my_socket.connect(("127.0.0.1", 8820))
mesage = ""
while mesage != "exit":
    mesage = input("write mesage:")
    my_socket.send(mesage.encode('utf-8'))
    data = my_socket.recv(1024)
    data = data.decode('utf-8')
    print(data)
my_socket.close()
