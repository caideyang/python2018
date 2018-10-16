#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/27 20:29

from concurrent.futures import ProcessPoolExecutor # d导入进程池模块
from concurrent.futures import ThreadPoolExecutor #导入线程池模块
from threading import currentThread
import time
def task(name):
    time.sleep(3)
    print(name, currentThread())

if __name__ == "__main__":
    # pool = ThreadPoolExecutor(5)
    # for i in range(20):
    #     pool.submit(task, 'caideyang')
    # pool.shutdown()
    # print("main", currentThread())



    from multiprocessing import Queue
    q = Queue(2)
    q.put("abc", block=True, timeout=None)
    q.put("abc", block=True, timeout=None)
    q.put("abc", block=True, timeout=1)
