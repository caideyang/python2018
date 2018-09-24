#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/24 14:18


hight = 100

total = 100
for  i in range(1,10):
    hight /= 2
    total += hight * 2

    print("第%s次落下弹起的高度为%s" %(i, hight))
print(total)