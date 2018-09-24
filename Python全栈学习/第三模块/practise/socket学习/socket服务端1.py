#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/18 21:56


import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8080))
server.listen()
conn, addr = server.accept()
while True:
    data = conn.recv(1024)
    print(data.decode('utf-8'))
    send_data = input("Server: ").strip()
    conn.send(send_data.encode('utf-8'))