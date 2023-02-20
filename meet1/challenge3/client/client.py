import socket

server_address = ('localhost', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

while True:
    f = open(fileName, 'r')
    msg = f.read()
    f.close()

    clinet_socket.send(msg.encode())
    ack = client_socket.recv(1024).decode()
    print(ack)

    clinet_socket.close()
