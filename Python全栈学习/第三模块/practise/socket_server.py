#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/14 13:47

#
# if __name__ == "__main__":
#     pass

import socket
server = socket.socket()
server.bind(("localhost", 8080))
server.listen()
while True:
    conn, addr = server.accept()
    print(conn)
    print(addr)
    data = conn.recv(1024)
    conn.close()