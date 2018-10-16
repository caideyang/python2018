#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/10/10 21:46

from threading import  Thread
import time
from datetime import datetime
"""
写一个程序，包含十个线程，子线程必须等待主线程sleep 10秒钟之后才执行，并打印当前时间；
"""
def task():
    print(datetime.now())


if __name__ == "__main__":
    time.sleep(10)
    print("main")
    for i in range(10):
        t = Thread(target=task)
        t.start()
