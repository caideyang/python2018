#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/7 20:23

name = 'caideyang'

print(all([1,2,3,4,0])) #False
print(any([1,2,3,4,0])) #True
print(abs(-5))  #5
print(dict(name='caideyang',age=31)) #{'name': 'caideyang', 'age': 31}
print(min([1,2,3,4,5]))  #1
print(max([1,2,3,4,5]))  #5
print(dir())  #列出所有的对象
print(hex(12))  #将数字转换为16进制
print(oct(12))  #将数字转换为8进制
print(bin(15))  #将数字转换为二进制
print(eval('123')) #123
print(ord('a')) #返回字符在ascii码中对应的位置
print(sum([1,2,3,4,5])) # 15 求和
print(bytearray("蔡德阳".encode('utf-8')))
