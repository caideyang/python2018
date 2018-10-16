#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/26 17:10
from threading import  Thread
import time
def task():
    print("1111111111")
    time.sleep(2)
    print("22222222222")

if __name__ == "__main__":
    t = Thread(target=task)
    t.setDaemon(True)
    t.start()
    t2 = Thread(target=task)
    t2.start()
    print(t.isAlive())
    print("主线程执行结束")