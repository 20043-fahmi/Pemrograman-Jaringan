import socket
import sys
import time

server_address = ('localhost', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)

try:
    while True:
        client_socket, client_address = server_socket.accept()

        data = client_socket.recv(1024).decode()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        dataRecv = str(client_address[0] + "-" + str(timestamp) + str(data))

        if data == 'asklog':
            f = open("log.txt", "a")
            msg = f.read()
            client_socket.send(msg.endcode())
        else:
            f = open("log.txt", "a")
            f.write(dataRecv)
            f.close()

            client_socket.send(dataRecv.encode())

        print(client_address)

except KeyboardInterrupt():

    server_socket.close()
    sys.exit(0)
