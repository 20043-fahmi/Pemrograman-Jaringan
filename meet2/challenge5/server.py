import socket
import select
import sys

server_address = ('127.0.0.1', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

input_socket = [server_socket]

try:
    while True:
        read_ready, write_ready, exception = select.select(
            input_socket, [], [])

        for sock in read_ready:
            if sock == server_socket: # Jika socket yang mengirim input adalah socket server
                client_socket, client_address = server_socket.accept()
                input_socket.append(client_socket)
            else: # Jika socket yang mengirim input adalah socket client
                nameFile = sock.recv(1024).decode() # Menerima input dari client
                with open(nameFile, 'r') as file: # Membuka file yang diinputkan
                    data = file.read() # Membaca isi file
                # print(str(sock.getpeername()), str(
                #     data) + "=" + str(eval(data)))
                lines = data.splitlines() # Membagi isi file menjadi baris
                for line in lines: # Mengecek setiap baris
                    print(str(line), 
                          'PALINDROME') if line == line[::-1] else print(str(line), 'NOT PALINDROME')
                    # Mengecek apakah baris tersebut palindrome atau bukan
                    f = open("file.txt", "a")
                    f.write (str(line), 
                          'PALINDROME') if line == line[::-1] else print(str(line), 'NOT PALINDROME')
                if str(data): 
                    client_socket.send(data.encode()) 
                else:
                    sock.close()
                    input_socket.remove(sock)


except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)


# string = input('Enter anything: ')

print('PALINDROME') if string == string[::-1] else print('NOT PALINDROME')
