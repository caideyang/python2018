#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/25 15:38

# from multiprocessing import Process
# import time
# import os
#
# def task():
#     print("Task %s is running,PPID is %s ..." %(os.getpid(), os.getppid()))
#     time.sleep(3)
#     print("Task %s is end..." % os.getpid())
#
# if __name__ == "__main__":
#     p1 = Process(target=task)
#     p2 = Process(target=task)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join() # join方法执行完以后再执行后面的进程
#     print("父进程", os.getpid())



# from multiprocessing import Process
# import time
# import os
#
# def task():
#     print("Task %s is running,PPID is %s ..." %(os.getpid(), os.getppid()))
#     time.sleep(10)
#     print("Task %s is end..." % os.getpid())
#
# if __name__ == "__main__":
#     p1 = Process(target=task)
#     p2 = Process(target=task)
#     p1.start()
#     p2.start()
#     p1.terminate()
#     print(p1.is_alive())
#     time.sleep(1)
#     print(p1.is_alive())
#     p1.join()
#     p2.join() # join方法执行完以后再执行后面的进程
#     print("父进程", os.getpid())


from multiprocessing import Process
import time
import os

def task():
    print("Task %s is running,PPID is %s ..." %(os.getpid(), os.getppid()))
    time.sleep(10)
    print("Task %s is end..." % os.getpid())

if __name__ == "__main__":
    p1 = Process(target=task, name="进程1")  # name指定进程的名字
    p2 = Process(target=task, name="进程2")  # name 指定进程的名字
    p1.start()
    p2.start()
    print(p1.name, p1.pid)  # p.pid获取该子进程的pid，等同于os.getpid()
    print(p2.name, p2.pid)  # p.pid获取该子进程的pid，等同于os.getpid()
    p1.join()
    p2.join() # join方法执行完以后再执行后面的进程

    print("父进程", os.getpid())






