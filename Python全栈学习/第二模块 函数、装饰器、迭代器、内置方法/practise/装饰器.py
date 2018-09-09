#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/7 19:53

import time

def login(func):
    def inner(*args,**kwargs):
        name = input("Your name: ").strip()
        passwd = input("Your password: ").strip()
        if name == 'alex' and passwd == '123':
            print("登陆成功！")
            return func(*args,**kwargs)
        else:
            print("用户名密码错误！")
    return inner

def get_time(func):
    def inner(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print("%s 函数执行用时: %s" % (func, end_time - start_time))
    return inner

@login
def index():
    time.sleep(2)
    print("主页")

if __name__ == "__main__":
    index()