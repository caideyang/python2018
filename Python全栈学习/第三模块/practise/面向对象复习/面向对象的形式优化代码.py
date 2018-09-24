#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/24 16:32

class MySql(object):
    def __init__(self, host, port, charset):
        self.host = host
        self.port = port
        self.charset = charset
        self.conn = self.connect()

    def connect(self):
        print("已经连接数据库IP:%s，端口号:%s,字符集：%s ...." % (self.host, self.port, self.charset))

    def excute(self, sql):
        return 'excute: %s' % sql

    def call_proc(self, sql):
        return 'call_proc: %s' %sql


db = MySql('127.0.0.1', 3306, 'utf-8')
print(db.excute("select * from test"))
print(db.call_proc("update test set name='caideyang'"))