#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/30 9:52

"""
阶乘
"""
def get_factorial(n):
    if n == 1:
        return n
    else:
        return n * get_factorial(n - 1)

print(get_factorial(5))