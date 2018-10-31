#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/26 14:57

import select
import socket
import queue

server = socket.socket()
server.bind(("localhost",9000))
server.listen(100) #开始监听，最多允许100个连接
server.setblocking(False) #设置为非阻塞

msg_dic = {}
inputs = [server,]
outputs = []

while True:
    readable,writeable,exceptional = select.select(inputs,outputs,inputs)
    # print(readable, writeable, exceptional)
    for r in readable:
        if r is server:  #代表来了一个新连接
            conn,addr = server.accept()
            print("接入一个新的连接",addr)
            inputs.append(conn) #要想实现这个客户端发数据来时server端能知道，就需要让select再监测这个conn
            msg_dic[conn] = queue.Queue()  # 初始化一个队列，后面存要返回给这个客户端的数据
            # print(msg_dic)
        else:  #当r不为server时就代表有数据接收
            try: #try catch捕捉异常，当客户端异常断开时
                data = r.recv(1024) #接收数据
                if data:
                    print("收到 %s 的数据为【%s】" %(r,data.decode()))
                    msg_dic[r].put(data) #将要发送的消息放入到队列中
                    if r not in outputs:
                        outputs.append(r) #将需要返回消息的连接放入output列表
                else: #当data为空，断开连接
                    if r not in exceptional:
                        exceptional.append(r)
            except ConnectionResetError as e:
                exceptional.append(r)
    for w in writeable:   #要返回给客户端的连接列表
        data_to_client = msg_dic[w].get() #从消息队列中取出需要发送给客户端的消息
        w.send(data_to_client) #将消息返回给客户端
        outputs.remove(w)  #确保下次循环完成，不再处理这个已经处理完的消息

    for e in exceptional: #连接异常的socket连接信息会自动存入到exceptional列表中
        print("%s客户端已经断开" % e)
        if e in outputs:
            outputs.remove(e) #将异常连接从outputs中移除
        inputs.remove(e)   #将异常连接从inputs中移除
        del msg_dic[e]  #删除对应的异常socket连接的队列


# if __name__ == "__main__":
#     pass