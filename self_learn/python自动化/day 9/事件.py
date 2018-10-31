#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/23 10:22

import threading
import time,random
event = threading.Event()
def lighter():
    if not event.isSet():  #
        event.set() #假设该状态，绿灯
    count = 0
    while True:
        if count < 10:
            print('\033[42;1m--green light on---\033[0m')
        elif count < 12:
            print('\033[43;1m--yellow light on---\033[0m')
        elif count < 20:
            if event.isSet():
                event.clear()#假设该状态红灯
            print('\033[41;1m--red light on---\033[0m')
        else:
            count = 0
            event.set()
        time.sleep(1)
        count += 1
def car(n):
    time.sleep(random.randrange(3))
    if event.isSet():
        print("Car [%s] is running...." % n)
    else:
        print("Car [%s] is waiting...." % n)
light = threading.Thread(target=lighter)
light.start()
while True:
    time.sleep(1)
    n = random.randrange(1000,9000)
    t = threading.Thread(target=car,args=(n,))
    t.start()