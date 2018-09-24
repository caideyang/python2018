#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/27 21:59


"""
12. 写一个三次认证（编程）（10分钟）
  1. 实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次

"""
count = 0
names = ['seven','alex']
# while True:
#     if count == 3:
#         break
#     name = input("Pls. insert you name: ").strip()
#     passwd = input("Pls. insert you passwd: ").strip()
#     if name in names and passwd == '123':
#         print("登陆成功！")
#         break
#     else:
#         print("登陆失败！")
#         count += 1
while count < 3:
    name = input("name: ").strip()
    passwd = input("passwd: ").strip()
    if name in names and passwd == '123':
        print("登陆成功")
        break
    else:
        print("登陆失败")
        count += 1
