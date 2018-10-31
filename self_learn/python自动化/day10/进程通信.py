#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/24 13:56

# from multiprocessing import Process,Queue
#
# def run(q):
#     q.put("Fuck!")
#
# if __name__ == "__main__":
#     q = Queue()
#     p = Process(target=run,args=(q,))
#     p.start()
#     print(q.get())
#     p.join()


from multiprocessing import Process ,Pipe
def f(conn):
    conn.send("hello papa")
    print("Son received: ",conn.recv())
    conn.close()

if __name__ == "__main__":
    p_conn,s_conn = Pipe()
    s_process = Process(target=f,args=(s_conn,))
    s_process.start()
    print("Parent received: ",p_conn.recv())
    p_conn.send("hello son")
    s_process.join()
    p_conn.close()