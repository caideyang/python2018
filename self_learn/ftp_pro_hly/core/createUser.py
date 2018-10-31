#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Han Liyue"


import configparser
import hashlib
import os

from conf import settings

class User:
    def __init__(self):
        self.cUser()

    # 创建用户名、md5、存储空间大小、用户自己的目录
    def cUser(self):
        username = input('user_name：>>>').strip()
        password = input('pwd：>>>').strip()
        size = input('size：>>>').strip()

        # 密码加密
        # 2.将密码进行加密
        h = hashlib.md5()  # 创建一个hash对象，hashlib.md5()可换位sha256()
        h.update(bytes(password, encoding='utf-8'))
        pawd_result = h.hexdigest()  # 获取加密结果


        # 写到配置文件中
        conf = configparser.ConfigParser()
        conf.add_section(username)
        conf[username]['name'] = username
        conf[username]['passwd'] = password
        conf[username]['passwdMD5'] = pawd_result
        conf[username]['stronage_size'] = size
        conf.write(open(settings.account_file, 'a'))
        print('%s userinfo insert successful'%username)
        self.add_list(username)

    # 添加用户信息
    def add_list(self, username):
        # 用户信息存放路径
        owm_path = settings.public_list
        # 命名
        os.mkdir('%s\\%s' % (owm_path, username))

user = User()
