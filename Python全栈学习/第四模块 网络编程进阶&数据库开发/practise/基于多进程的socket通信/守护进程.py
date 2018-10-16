#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/25 17:56

from multiprocessing import Process

import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':
    p1=Process(target=foo)
    p2=Process(target=bar)

    p1.daemon=True
    p1.start()
    p2.start()
    # time.sleep(2)
    print("main-------")