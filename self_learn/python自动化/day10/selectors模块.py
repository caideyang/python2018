#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/27 6:01

import selectors
import socket


def accept(sel,sock,mask):  #客户端连接，注册到selectors
    conn,addr = sock.accept()
    print('accepted', conn, 'from', addr, mask)
    conn.setblocking(False) #设置非阻塞模式
    sel.register(conn,selectors.EVENT_READ,read) #新连接注册read函数

def read(sel,conn,mask):  #客户端数据处理函数
    try:
        data = conn.recv(1024)
        if data:
            print(repr(data),"from ",conn)
            conn.send(data)
        else:
            print("Closing ",conn)
            sel.unregister(conn)
            conn.close()
    except ConnectionResetError as e:
        print(e)
        print("Closing ", conn)
        sel.unregister(conn)
        conn.close()

sel = selectors.DefaultSelector()  #创建一个selectors对象实例
sock = socket.socket()
sock.bind(('0.0.0.0',9000))
sock.listen(100)
sock.setblocking(False)
sel.register(sock,selectors.EVENT_READ,accept) #将创建的socket服务注册到sel，并通过事件进行客户端注册
while True:
    events = sel.select() #默认阻塞，有活动连接就返回活动的连接列表
    for key,mask in events:
        callback = key.data #accept
        callback(sel,key.fileobj,mask) #key.fileobj=  文件句柄，回调函数，将参数sel,key.fileobj,mask传给accept函数

