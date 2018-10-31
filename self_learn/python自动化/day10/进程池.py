#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/25 5:32

from multiprocessing import Process,Pool
import time,os
def foo(n):
    print("进程ID[%s]输出的结果为[%s]" %(os.getpid(),n+2))
    time.sleep(1)
    return n+2
def bar(m):
    print("bar函数的进程ID[%s],参数m的值为[%s]" %(os.getpid(),m))

if __name__ == "__main__":
    pool = Pool(processes=3) #创建一个进程池，包含五个进程
    print("z主进程ID:%s" % os.getpid())
    for i in range(10):
        # pool.apply(func=foo,args=(i,))
        pool.apply_async(func=foo,args=(i,),callback=bar) #callback为回调函数，其参数为子进程中foo函数的返回值，回调函数在主进程中执行

    pool.close()
    pool.join()

    print("end")
