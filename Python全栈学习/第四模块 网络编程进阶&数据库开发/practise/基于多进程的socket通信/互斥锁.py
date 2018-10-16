#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/25 17:59

#并发运行,效率高,但竞争同一打印终端,带来了打印错乱
from multiprocessing import Process, Lock
import os,time
def work(lock):
    lock.acquire()
    print('%s is running' %os.getpid())
    time.sleep(2)
    print('%s is done' %os.getpid())
    lock.release()

if __name__ == '__main__':
    lock = Lock()

    for i in range(3):
        p=Process(target=work, args=(lock, ))
        p.start()
