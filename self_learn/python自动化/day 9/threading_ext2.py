#encoding:utf-8
import threading,time

class MyThread(threading.Thread):
    def __init__(self,n,st):
        super(MyThread,self).__init__() #继承父类的init方法
        self.n = n
        self.sleep_time = st
    def run(self): #必须调用run函数
        print("Task%s,current thread is %s" %(self.n,threading.current_thread())) #threading.current_thread()获取当前线程
        time.sleep(self.sleep_time)
        print("Task %s done" %self.n)
        print(threading.active_count()) #打印活动的线程

start_time = time.time()
t1 = MyThread("t1",2)
t2 = MyThread("t2",4)
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.time()
print("main thread!")
print("Cost: %s" %(end_time-start_time))