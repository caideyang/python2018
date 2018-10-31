#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/25 7:08
import gevent
import time

def foo():
    print("foo begin")
    gevent.sleep(5) #只要有sleep即跳到其他协程
    print("foo end")
def bar():
    print("bar begin")
    gevent.sleep(4)#只要有sleep即跳到其他协程
    print("bar end")
def fun():
    print("fun begin")
    gevent.sleep(2)#只要有sleep即跳到其他协程
    print("fun end")
if __name__ == "__main__":
    begin_time = time.time()
    gevent.joinall([         #使用gevent，列表传入两个协程
        gevent.spawn(foo),   #生成一个协程
        gevent.spawn(bar),
        gevent.spawn(fun),
    ])
    end_time = time.time()
    print("Time Cost: %s "%(end_time-begin_time))