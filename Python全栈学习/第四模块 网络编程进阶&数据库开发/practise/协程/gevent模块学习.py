#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/28 11:53

from gevent import monkey; monkey.patch_all() # 导入该模块则遇到所有的io阻塞自动切换
import gevent
import time
def eat(name):
    print("%s is eating" % name)
    time.sleep(1)
    # gevent.sleep(1)
    print("%s is eating" % name)
def play(name):
    print("%s is playing " % name)
    time.sleep(3)
    # gevent.sleep(1)
    print("%s is playing " % name)
if __name__ == "__main__":
    g1 =gevent.spawn(eat, 'Alex')
    g2 = gevent.spawn(play, "egon")
    g1.join()
    g2.join()
    # 或者 gevent.joinall([g1,g2])