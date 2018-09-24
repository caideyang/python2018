#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/23 13:11

count = 0
for i in range(1,101):
    if i % 2 == 1:
        count += i
    else:
        count -= i
print(count)