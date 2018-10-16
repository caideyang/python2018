#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/26 15:54

from threading import Thread
import time

def task():
    print("Hello,This is a task")
    time.sleep(1)
    print("This is task end")

if __name__ == "__main__":
    t = Thread(target=task,)
    t.start()

    print("main process")