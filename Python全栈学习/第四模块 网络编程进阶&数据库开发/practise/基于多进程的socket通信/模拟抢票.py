#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/26 10:16

from multiprocessing import Process
from multiprocessing import Lock
import time
import json
def search(name):
    time.sleep(0.5)
    count = json.load(open("ticket.json", "r"))['count']
    print("%s查询到余票%s" %(name, count))

def buy(name, lock):
    search(name)
    lock.acquire() # 加锁
    count = json.load(open("ticket.json", "r"))['count']
    count -= 1
    time.sleep(1)
    if count >= 0:
        print("%s买票成功！剩余票数%s" % (name, count))
        with open("ticket.json", "w") as f:
            json.dump({"count": count}, f)
    else:
        print("%s买票失败！剩余票数为0" % name)
    lock.release() # 锁释放

if __name__ == "__main__":
    lock = Lock()

    for i in range(10):
        name = "用户%s" % i
        p = Process(target=buy, args=(name, lock))
        p.start()