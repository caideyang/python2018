#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/26 10:41

from multiprocessing import Queue
import time
if __name__ == "__main__":
    q = Queue(3)  # 创建队列，最大深度3
    q.put("hello")  # 往队列存放消息
    q.put([1,2,3,4])
    q.put({"name": "caideyang"})
    # time.sleep(1)
    print(q.empty()) # 判断队列是否为空
    print(q.full())  # 判断队列是否满了
    print(q.get())   # 从队列取数据
    print(q.get())