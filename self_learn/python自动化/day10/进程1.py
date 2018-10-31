#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/24 13:08

import multiprocessing,threading
import time
def thread_run():
    print("This is thread %s" %threading.get_ident())

def run(n):
    print("run %s" %n)
    t= threading.Thread(target=thread_run,)
    t.start()
    time.sleep(2)
    print("done!")

if __name__ == "__main__":
    print("Begin!")
    p_list = []
    for i in range(10):
        p = multiprocessing.Process(target=run,args=(i,))
        p.start()
        p_list.append(p)
    for p in p_list:
        p.join()
    print("Finish!")