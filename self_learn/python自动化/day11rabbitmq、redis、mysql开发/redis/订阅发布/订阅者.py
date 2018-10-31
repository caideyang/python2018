#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/30 16:41


from monitor import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg = redis_sub.parse_response()
    print(msg)