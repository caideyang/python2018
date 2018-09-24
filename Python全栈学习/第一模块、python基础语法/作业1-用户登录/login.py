#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/22 16:19

  # 用户列表
user_list = [("caideyang","111111"),("deyangcai","123456")]
  # 已锁定用户列表
lock_list = []
with open("lock_user",'r+') as f:
    for user in f.readlines():
        lock_list.append(user.strip())
# print(lock_list)
  # 登录次数
count = 0
while True:
    while count < 3:  # 当重试次数少于三次
        username = input("Pls. insert your name: ").strip()
        if username in lock_list:
            exit("当前用户%s 被锁定，程序退出..." % username)
        password = input("Pls. insert you passwd: ").strip()
        if (username, password) not in user_list:
            print("用户名或密码错误，请重试")
            count += 1
            break
        else:
            # print("登录成功！欢迎【%s】登录！" % username)
            exit("登录成功！欢迎【%s】登录！" % username)
    else:
        print("用户名或密码输入错误次数达到3次，用户已锁定！")
        with open('lock_user','a+') as f:
            f.write(username+'\n')
        break

