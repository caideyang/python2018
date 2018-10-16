#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/25 14:18



from multiprocessing import Process
import time
import os

def task():
    print("Task %s is running,PPID is %s ..." %(os.getpid(), os.getppid()))
    time.sleep(3)
    print("Task %s is end..." % os.getpid())

if __name__ == "__main__":
    p1 = Process(target=task)
    p2 = Process(target=task)
    p1.start()
    p2.start()
    print("父进程", os.getpid())

# from multiprocessing import Process
# import time
# # 通过改写Process类来实现自己的多进程并发功能
# class MyProcess(Process):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):  # MyProcess子类里面必须用run方法作为其执行方法
#         starttime = time.time()
#         print("Task %s is running ..." % self.name)
#         time.sleep(3)
#         print("Task %s is end..." % self.name)
#         endtime = time.time()
#         print("Task %s cost %s seconds ..." %(self.name, endtime - starttime))
#
# if __name__ == "__main__":
#     p1 = MyProcess('子进程1')
#     p2 = MyProcess('子进程2')
#     p1.start()
#     p2.start()
#     print("父进程")
