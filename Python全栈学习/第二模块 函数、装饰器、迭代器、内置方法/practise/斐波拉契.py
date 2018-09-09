#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/7 21:15



def febolaqi(num):
    n,a,b = 0,0,1
    while n < num:
        # print(b)
        yield b
        a, b = b, a+b
        n += 1
        # yield b

res = febolaqi(100)
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
for i in res:
    print(i)