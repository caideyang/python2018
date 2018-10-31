#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/6 15:22

a = "acb"
b = 456
def  getname(num):
    global  a
    a = "123"
    b = num
    print(b)
getname(678)
print(a,b)
# print(a)
print(globals())
print(locals())
# print(help(locals()))


if __name__ == "__main__":
    pass