#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/26 14:11


from multiprocessing import Process, Lock
import  os
import time
def task(lock):
    lock.acquire() # 加锁
    print("%s is running !" %os.getpid())
    time.sleep(1)
    print("%s is over !" % os.getpid())
    lock.release() # 锁释放

if __name__ == '__main__':
    lock = Lock()  # 创建一个锁对象
    for i in range(3):
        p = Process(target=task, args=(lock, ))
        p.start()