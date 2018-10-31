#encoding:utf-8
import socket

client = socket.socket() #申明Socket类型，同时生产socket连接
client.connect(('localhost',9000))
while True:
    msg = input(">>>").strip()
    if len(msg) == 0 : continue
    if msg.upper() == 'EXIT' :   exit("连接断开！")
    client.send(msg.encode("utf-8")) #需要发送byte类型的数据,如果有中文，则用encode()转换
    data = client.recv(8192)
    print("recv: %s" % data.decode()) #使用decode转换回中文