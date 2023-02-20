import socket
server_address = ('localhost', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

while True:
    strsend = input("Enter the message:")
    client_socket.send(strsend.encode())

    data = client_socket.recv(1024).decode()

    print(data)

client_socket.close()
