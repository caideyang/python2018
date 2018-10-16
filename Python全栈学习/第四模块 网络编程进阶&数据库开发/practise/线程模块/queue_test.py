#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/28 6:37

# from queue import Queue

if __name__ == "__main__":
    import queue
    q = queue.Queue(2)
    q.put(1)
    q.put(2)
    q.put(2)

    # q.put(4)