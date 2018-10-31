#encoding:utf-8

import threading,time
def run(args):
    print("Task ",args)
    time.sleep(1.4999999)
    print("Task %s done" % args )
start_time = time.time()
#启动多个线程
for n in range(50):
    t = threading.Thread(target=run,args=(str(n),))
    t.setDaemon(True) #把当前线程设置为守护线程
    t.start()
end_time = time.time()
print("----All threads have finished !---")
print("Cost: %s" %(end_time-start_time))
time.sleep(1.5)