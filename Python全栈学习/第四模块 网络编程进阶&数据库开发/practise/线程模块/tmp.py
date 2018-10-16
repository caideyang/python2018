
#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/10/10 14:15


from multiprocessing import Process
from threading import Thread
import os,time

def work():
    res=0
    for i in range(100000000):
        res*=i


if __name__ == '__main__':
    l=[]
    print(os.cpu_count()) #本机为4核
    start=time.time()
    for i in range(4):
        p=Process(target=work) #耗时5s多3.7150588035583496
        # p=Thread(target=work) #耗时18s多14.295367002487183
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop=time.time()
    print('run time is %s' %(stop-start))