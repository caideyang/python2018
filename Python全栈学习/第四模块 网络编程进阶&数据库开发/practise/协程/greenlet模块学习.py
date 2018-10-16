#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/28 11:15
from greenlet import greenlet

def eat(name):
    print("%s is eating" % name)
    g2.switch(name)
    print("%s is eating" % name)
    g2.switch()
def play(name):
    print("%s is playing " % name)
    g1.switch(name)
    print("%s is playing " % name)
if __name__ == "__main__":
    g1 = greenlet(eat)
    g2 = greenlet(play)
    g1.switch("Alex")

