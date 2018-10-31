#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/23 9:20

import threading,time

single = threading.BoundedSemaphore(5)  #创建五个信号量,设置最大5个子线程并发运行
def run(n):
    single.acquire()
    print("---- %s" %n)
    time.sleep(1)
    single.release()


for i in range(22):
    t = threading.Thread(target=run,args=(i,))
    t.start()