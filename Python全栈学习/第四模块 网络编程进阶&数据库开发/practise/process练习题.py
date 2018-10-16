#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/25 16:46

from multiprocessing import Process
import time
import random

def task(n):
    time.sleep(random.randint(1,3))
    print('-------->%s' %n)

if __name__ == '__main__':
    p1=Process(target=task,args=(1,))
    p2=Process(target=task,args=(2,))
    p3=Process(target=task,args=(3,))

    p_list = [p1, p2, p3]
    for p in p_list:  # 串行
        p.start()
    # for p in p_list:  # 并行
        p.join()

    print('-------->4')
