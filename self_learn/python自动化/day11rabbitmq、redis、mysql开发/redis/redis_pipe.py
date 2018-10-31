#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/30 16:10

import redis

pool = redis.ConnectionPool(host='192.168.56.11', port=6379)

r = redis.Redis(connection_pool=pool)
pipe = r.pipeline()
# pipe = r.pipeline(transaction=True)

pipe.set('name', 'alex111')
pipe.set('role', 'sb')

pipe.execute()