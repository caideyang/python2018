#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/10/30 12:41

from socket import *

def handler(client):
    try:
        recv_data = client.recv(1024)
        print(recv_data.decode("utf-8"))
        client.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf8"))
        with open("static\index.html", 'rb') as f:
            for line in f:
                client.send(line)
                # print(line.decode('utf-8'))
    except Exception as e:
        print(e)


def main(ip, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(10)
    while True:
        client, addr = server.accept()
        print(addr)
        handler(client)


if __name__ == "__main__":
    main('localhost', 9000)