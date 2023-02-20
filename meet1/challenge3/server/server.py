import socket
import sys
import time

server_address = ('localhost', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)

try:
    while True:
        client_socket, client_adrress = server_socket.acceot()

        fileName = client_socket.recv(1024).decode()
        print()

        f = open(fileName, 'r')
        msg = fread()
        f.close()

        client_socket.send(msg.encode())

        isiFile = client_socket.recv(1024).decode()
        print(isiFile)

        f = open(fileName, 'w')
        f.write(isiFile)
        f.close()

except KeyboardInterrupt:
    server.socket.close()
    server_address.close()
    print("Server is terminated")
    sys.exit(0)
