#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/30 16:40


import redis
class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='192.168.56.11')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'
    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True
    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub
