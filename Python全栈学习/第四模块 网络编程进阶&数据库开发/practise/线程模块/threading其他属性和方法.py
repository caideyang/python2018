#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/26 16:53

from threading import  Thread
import threading
import time
import random
import os

def task():
    print("hello")
    time.sleep(random.randint(1,5))
    print("end")

if __name__ == "__main__":
    t1 = Thread(target=task)
    t2 = Thread(target=task)
    t3 = Thread(target=task)
    t1.start()
    t2.start()
    t3.start()
    t3.join()
    t2.join()
    t1.join()
    print(t1.isAlive())  # t.is_alive() 同 t.isAlive()
    t1.setName("线程1")
    print(t1.getName())
    print(os.getpid())
    print(threading.currentThread().getName())
    time.sleep(3.5)
    print(threading.active_count())
    print(threading.enumerate())  # 返回一个列表，列表里展示所有