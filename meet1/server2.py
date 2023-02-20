import socket
import sys

server_address = ('localhost', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)


try:
    while True:
        client_socket, client_address = server_socket.accept()
        print('Connection from:', client_address)
        print('Connection from:', client_socket)

        data = client_socket.recv(1025).decode()
        print(str(data))

        client_address.close()

except KeyboardInterrupt:
    print('server stopped')
    server_socket.close()
    sys.exit(0)
