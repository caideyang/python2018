#encoding:utf-8

import threading,time

num = 0

def run(n):
    global num
    lock.acquire()
    print(threading.current_thread())
    num += 1
    # time.sleep(1)
    lock.release()
    print(num)

lock = threading.Lock()
for i in range(50):
    t = threading.Thread(target=run,args=(i,))

    t.start()

print(num)