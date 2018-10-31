#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/30 16:44

from monitor import RedisHelper

obj = RedisHelper()
while True:
    message = input(">>>")
    obj.public(message)