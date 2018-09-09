#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/4 16:22

import os
import json
from conf import settings
from core import logger

def login_required(func):
    "验证用户是否登录"

    def wrapper(*args,**kwargs):
        #print('--wrapper--->',args,kwargs)
        if args[0].get('is_authenticated'):
            return func(*args, **kwargs)
        else:
            print("User is not authenticated.")
            login()
    return wrapper


def acc_auth(account, password, type='shopping'):
    data_dir = settings.DATABASE[type]
    file_name = '%s/%s.json' %(data_dir,account)
    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            data = json.load(f)
            # print(data)
        if account == (data['account'] if type=='shopping' else str(data['id'])) and password == data['password']:
            print("账户验证成功！")
            return data
        else:
            print("账户验证失败！")
    else:
        print("账号不存在")

def login(user_data,log_obj):
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3 :
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth = acc_auth(account, password,'shopping')
        if auth: #not None means passed the authentication
            user_data['is_authenticated'] = True
            user_data['account'] = account
            log_obj.info("account [%s] login successfully !" % account)
            #print("welcome")
            return auth
        retry_count +=1
    else:
        log_obj.error("account [%s] too many login attempts" % account)
        exit()


if __name__ == "__main__":
    pass