#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/24 16:31

from multiprocessing import Process,Lock

def run(l,i):
    l.acquire()
    print("process %s" %i )
    l.release()

if __name__=="__main__":
    lock = Lock()
    for i in range(10):
        p = Process(target=run,args=(lock,i))
        p.start()