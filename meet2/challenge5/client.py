import socket
import sys

server_address = ('127.0.0.1', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

sys.stdout.write('>> ')

try:
    while True:
        inputTest = str(input()) # Menerima input dari user kirim file yang mau di cek
        client_socket.send(inputTest.encode()) # Mengirim input ke server

except KeyboardInterrupt:
    client_socket.close()
    sys.exit(0)
