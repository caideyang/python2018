#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/26 16:00

from socket import *
from threading import currentThread, Thread
from concurrent.futures import ThreadPoolExecutor
def client(i):
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(("localhost", 9000))
    while True:
        data = "%s ======>%s" %(i, currentThread())
        client.send(data.encode('utf-8'))
        data = client.recv(1024).decode('utf-8')
        print(data)

if __name__ == "__main__":
    # pool = ThreadPoolExecutor(10000)
    # for i in range(5000):
    #     pool.submit(client, i)
    for i in range(5000):
        t = Thread(target=client, args=(i, ))
        t.start()