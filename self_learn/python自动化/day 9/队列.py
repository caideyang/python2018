#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/23 13:09

import queue,threading

# q = queue.Queue(maxsize=10) #设置队列最大深度，当超过时阻塞，直到队列里消息被消费，才能有新的消息写入
# q.put("disk1")
# q.put("disk2")
# print(q.qsize())
# print(q.get())
# print(q.qsize())
# print(q.get())
# print(q.qsize())
# print(q.get_nowait()) #当没有数据时报错
# print(q.get(timeout=1)) #等待一秒，如果没有数据则报错

# Q = queue.LifoQueue() #创建一个后进先出队列
# Q.put("hello1")
# Q.put("hello2")
# Q.put("hello3")
# print(Q.get())
# print(Q.get())
# print(Q.get())

q = queue.PriorityQueue() #创建优先级队列
q.put((10,"caideyang"))
q.put((2,"abc"))
q.put((3,"Vbc"))
q.put((5,"Fbc"))
print(q.get())
print(q.get())
print(q.get())
print(q.get())
