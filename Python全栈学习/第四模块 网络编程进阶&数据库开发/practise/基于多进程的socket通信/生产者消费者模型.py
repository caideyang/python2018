#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/26 11:50

from multiprocessing import  Process, Queue
import time
def producer(name, q):
    for i in range(10):
        time.sleep(0.5)
        res = "包子%s" %i
        print("%s 生产了%s" % (name, res))
        q.put(res)

def consumer(name, q):
    while True:
        res = q.get()
        if not res: break
        time.sleep(1)
        print("%s 正在吃%s" % (name, res))

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=producer, args=("张三", q))
    p2 = Process(target=producer, args=("李四", q ))
    p3 = Process(target=producer, args=("小万", q ))
    c1 = Process(target=consumer, args=("Alex", q ))
    c2 = Process(target=consumer, args=("Egon", q ))

    for i in [p1,p2,p3,c1,c2]:
        i.start()


