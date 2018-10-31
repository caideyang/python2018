#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/23 13:30

import threading,queue
import time
q = queue.Queue(maxsize=10)
def Producer(name):
    count = 1
    while True:
        q.put("包子%s" % count )
        print("包子%s生产成功" % count )
        count += 1
        # time.sleep(1)

def Consumer(name):
    # while q.qsize() > 0 :
    while True:
        print("%s 取到[%s]，并吃掉" %(name,q.get()))
        # time.sleep(1)


p = threading.Thread(target=Producer,args=('Alex',))
c1 = threading.Thread(target=Consumer,args=('czh',))
c2 = threading.Thread(target=Consumer,args=('ws',))
p.start()
c1.start()
c2.start()
