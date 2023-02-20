import socket  # Import library socket
import sys  # Import library sys
import time  # Import library time

server_address = ('localhost', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(server_address)
server_socket.listen(5)

print('Server is running on port', server_address[1])

try:
    while True:
        client_socket, client_address = server_socket.accept()

        data = client_socket.recv(1024).decode()
        timeStamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        dataRecv = str(server_address[1]) + '-' + str(timeStamp) + str(data)

        with open('log.txt', 'a') as f:
            f.write(dataRecv)
            f.write('\n')

        client_socket.close()


except KeyboardInterrupt:
    server_socket.close()
    print('Server stopped')
    sys.exit(0)
