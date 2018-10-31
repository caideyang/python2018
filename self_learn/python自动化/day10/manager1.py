#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/24 16:19

from multiprocessing import Process,Manager
import os
def run(d,l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
if __name__ == "__main__":
    with Manager() as manager:
        d = manager.dict()
        l = manager.list()
        p_list = []
        for i in range(10):
            p = Process(target=run,args=(d,l))
            p.start()
            p_list.append(p)
        for p in p_list:
            p.join()
        print(d)
        print(l)