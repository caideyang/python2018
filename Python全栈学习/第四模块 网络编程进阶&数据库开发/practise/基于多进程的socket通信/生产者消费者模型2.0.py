#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/26 11:50

from multiprocessing import  Process, JoinableQueue
import time

def consumer(name, q):
    while True:
        res = q.get()
        if not res: break
        time.sleep(1)
        print("%s 正在吃%s" % (name, res))
        q.task_done() # 发送信号给q.join()，说明已经从队列中取走一个数据并处理完毕了

def producer(name, q):
    for i in range(10):
        time.sleep(0.5)
        res = "包子%s" %i
        q.put(res)
        print("%s 生产了%s" % (name, res))
    q.join() # 等到消费者把自己放入队列中的所有的数据都取走之后，生产者才结束

if __name__ == "__main__":
    q = JoinableQueue()

    p1 = Process(target=producer, args=("张三", q))
    p2 = Process(target=producer, args=("李四", q ))
    p3 = Process(target=producer, args=("小万", q ))
    c1 = Process(target=consumer, args=("Alex", q ))
    c2 = Process(target=consumer, args=("Egon", q ))
    c1.daemon = True
    c2.daemon = True
    for i in [p1,p2,p3,c1,c2]:
        i.start()
    p1.join()
    p2.join()
    p3.join()
 # 1、主进程等生产者p1、p2、p3结束
 # 2、而p1、p2、p3是在消费者把所有数据都取干净之后才会结束
 # 3、所以一旦p1、p2、p3结束了，证明消费者也没必要存在了，应该随着主进程一块死掉，因而需要将生产者们设置成守护进程


