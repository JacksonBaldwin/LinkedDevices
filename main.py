import os
import socket

HOST = 'localhost'
PORT = 65432

os.system('clear')
mode = input('setup mode: ')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    if mode == 'h': #run program as host, establish socket
        s.bind((HOST,PORT))
        print('bounded to ' + str((HOST,PORT)) + ', waiting for connection...')
        s.listen()
        conn, addr = s.accept()

        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                print('user:', data.decode())
                response = input('input message: ')
                conn.sendall(response.encode())

    if mode == 'c': #run program as client
        s.connect((HOST,PORT))
        while True:
            s.sendall(input('you: ').encode())
            data = s.recv(1024)
            print('host: '+data.decode())
