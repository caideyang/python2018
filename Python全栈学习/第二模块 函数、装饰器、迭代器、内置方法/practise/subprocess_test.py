#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/6 10:50


import subprocess

child = subprocess.Popen('ping  www.baidu.com',shell=True)
# child.wait()
print("parent process")

if __name__ == "__main__":
    pass