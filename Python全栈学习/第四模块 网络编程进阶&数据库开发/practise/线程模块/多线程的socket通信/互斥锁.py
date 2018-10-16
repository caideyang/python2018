#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/26 17:45

from threading import Thread
from threading import Lock
import time
n = 100
def task(lock):
    global n
    lock.acquire()
    temp = n
    time.sleep(0.01)
    n = temp - 1
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    t_l = []
    for i in range(100):
        t = Thread(target=task ,args=(lock, ))
        t_l.append(t)
        t.start()
    for t in t_l:
        t.join()

    print("n = ", n)
