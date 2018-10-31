#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/25 12:55

from urllib.request import urlopen
import gevent
from gevent import monkey

monkey.patch_all() #把当前程序的所有IO操作单独打一个标记，这样就可以使用多进程异步并行执行
def get_url(url):
    resp = urlopen(url)
    data = resp.read()
    with open(url.split(".")[1],"wb") as f:
        f.write(data)
    print(data)

if __name__ == "__main__":
    gevent.joinall([
        gevent.spawn(get_url,"https://www.baidu.com"),
        gevent.spawn(get_url, "http://www.sohu.com"),
        gevent.spawn(get_url, "http://www.51cto.com"),
    ])
