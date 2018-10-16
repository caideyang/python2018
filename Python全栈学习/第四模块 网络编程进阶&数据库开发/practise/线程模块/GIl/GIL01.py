#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/26 21:48

# from multiprocessing import Process
# from threading import Thread
# import os,time
# def work():
#     res=0
#     for i in range(100000000):
#         res*=i
#
#
# if __name__ == '__main__':
#     l=[]
#     print(os.cpu_count()) #本机为4核
#     start=time.time()
#     for i in range(12):
#         # p=Process(target=work) #耗时5s多
#         p=Thread(target=work) #耗时18s多
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#     stop=time.time()
#     print('run time is %s' %(stop-start))

from multiprocessing import Process
from threading import Thread
import threading
import os, time


def work():
    time.sleep(2)
    print('===>')


if __name__ == '__main__':
    l = []
    print(os.cpu_count())  # 本机为4核
    start = time.time()
    for i in range(400):
        p=Process(target=work) #耗时12s多,大部分时间耗费在创建进程上
        # p = Thread(target=work)  # 耗时2s多
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop = time.time()
    print('run time is %s' % (stop - start))