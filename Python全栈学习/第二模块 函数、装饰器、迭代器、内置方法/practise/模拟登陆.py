#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/30 10:06
f = open("user_info",'r',encoding="utf-8")
user_info = f.read()
print(user_info)
f.close()
f_lock = open("lock_user",'r',encoding="utf-8")
lock_user = f_lock.read()
f_lock.close()

while True:
    name = input("Pls. insert your name: ").strip()
    if name+"_" in user_info:
        print(name)
        if name in lock_user:
            print("该用户已锁定！")
            continue
        else:
            count = 0
            while count < 3:
                passwd = input("PLs. insert your passwd: ").strip()
                if name+"_"+passwd+"\n" in user_info:
                    exit("登陆成功！")
                else:
                    print("密码错误，请重试！")
                    count += 1
                    continue
            else:
                print("密码错误达到3次，已锁定！")
                f_lock = open("lock_user",'a',encoding="utf-8")
                f_lock.write(name)
                f_lock.close()
                exit()
    else:
        print("该用户不存在！")
        continue