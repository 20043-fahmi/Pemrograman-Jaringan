import socket
import select
import sys
# Membuat socket baru dengan protokol IPv4 dan TCP
server_address = ('127.0.0.1', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Membuat socket baru dengan protokol IPv4 dan TCP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Mengatur socket agar dapat digunakan kembali
server_socket.bind(server_address) # Menghubungkan socket ke server yang dituju
server_socket.listen(5) # Membuat socket menjadi socket yang dapat menerima koneksi

input_socket = [server_socket] # Membuat list untuk menyimpan socket yang terhubung ke server

# Menerima input dari user dan mengirimnya ke server
try:
    while True:
        # Menerima input dari user
        read_ready, write_ready, exception = select.select(
            input_socket, [], [])
        for sock in read_ready: # Jika socket yang terhubung ke server ada yang mengirim input
            if sock == server_socket: # Jika socket yang mengirim input adalah socket server
                client_socket, client_address = server_socket.accept() # Menerima koneksi dari client
                input_socket.append(client_socket) # Menambahkan socket client ke list
            else: # Jika socket yang mengirim input adalah socket client
                data = sock.recv(1024).decode() # Menerima input dari client
                print(str(sock.getpeername()), str(
                    data) + "=" + str(eval(data))) #print peername (ip,port) juga dengan hasil dari input
                f = open("file.txt", "a") # Membuka file untuk ditulis
                samaDengan = "="
                f.write(str(sock.getpeername()) + str(data.encode() + samaDengan.encode() + str(eval(data)).encode())) # Menulis hasil dari input ke file
                if str(data): # Jika input tidak kosong
                    client_socket.send(data.encode()) # Mengirim input ke client
                else:
                    sock.close() # Menutup socket
                    input_socket.remove(sock) # Menghapus socket dari list

# Ketika user menekan Ctrl+C, maka client akan menutup socket dan keluar dari program
except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)
