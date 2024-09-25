import requests
import os
import socket

HOST = 'localhost'
PORT = 65432

os.system('clear')
mode = input('setup mode: ')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    if mode == 'h': #run program as host

        s.bind((HOST,PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            print('Received:', data.decode())
            response = 'Hello from server!'
            conn.sendall(response.encode())

    if mode == 'c': #run program as client
        s.connect((HOST,PORT))
        s.sendall('Hello'.encode())
        data = s.recv(1024)
        print(data.decode())
