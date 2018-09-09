#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/30 22:40


is_authed = False
def login(func):
    def inner(*args,**kwargs):
        global is_authed
        if is_authed:
            print("用户已经登陆！")
            return func(*args,**kwargs)
        else:
            _username = "alex"
            _passwd = "123456"
            username = input("Pls. insert your name: ").strip()
            password = input("Pls. insert your passwd: ").strip()
            if username == _username and password == _passwd:
                is_authed = True
                print("登陆成功")
                return func(*args,**kwargs)
            else:
                print("用户名密码错误！")
    return inner
@login
def home():
    print("首页")

@login
def user_manage(name):
    print("用户管理: %s " % name )

@login
def news_manage(news,type="娱乐"):

    print("【%s】新闻报道: %s " %(type,news))

if __name__ == '__main__':
    home()
    user_manage("蔡德阳")
    news_manage("宝马男持刀砍人反被砍",type="法制周刊")

