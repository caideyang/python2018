#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/9 17:33

def range2(n):
    count = 0
    while count < n:
        print("count: %s" % count)
        count += 1
        sign = yield count
        print("-------Sign: %s" %sign)
        if sign == "stop":
            break
            # print("!!!!!!!!!!!!!!!!!!")
    return "ErrorCode:111"

new_range = range2(3)
#当调用next的时候，执行一次range2函数的while循环,然后count加1，并将count的结果存到生成器中
t1 = next(new_range)
print(t1)
#生成器的send()函数的作用：
#1.唤醒生成器并继续执行，等同与next()
#2.发送一条信息到生成器
t2 = new_range.send("send test .")
# print(t2)
# new_range.__next__()等价于next(new_range)
# new_range.send("stop")