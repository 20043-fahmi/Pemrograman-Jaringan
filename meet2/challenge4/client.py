import socket
import sys

server_address = ('127.0.0.1', 5000) # Membuat server dengan alamat IP dan port tertentu
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Membuat socket baru dengan protokol IPv4 dan TCP
client_socket.connect(server_address) # Menghubungkan socket ke server yang dituju


sys.stdout.write('>> ')

try: # Menerima input dari user dan mengirimnya ke server
    while True:
        inputTest = str(input()) # Menerima input dari user
        client_socket.send(inputTest.encode()) # Mengirim input ke server
        sys.stdout.write(client_socket.recv(1024).decode()) #print input dari server
        print(" =" + str(eval(inputTest))) #print hasil dari input

# Ketika user menekan Ctrl+C, maka client akan menutup socket dan keluar dari program
except KeyboardInterrupt:
    client_socket.close()
    sys.exit(0)
