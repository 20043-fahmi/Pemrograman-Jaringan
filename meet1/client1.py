import socket

server_address = ('localhost', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

strsend = 'Hello World'
client_socket.send(strsend.encode())
client_socket.close()
