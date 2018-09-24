#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/19 22:17

import socket
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8888))
server.listen(5)
while True:
    conn, addr = server.accept()
    while True:
        try:
            cmd = conn.recv(1024).decode('utf-8')
            if not cmd: break
            print(cmd)
            res = subprocess.Popen(cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE )

            stdout = res.stdout.read()
            stderr = res.stderr.read()
            conn.send(stdout + stderr)

        except ConnectionResetError:
            break
    conn.close()
