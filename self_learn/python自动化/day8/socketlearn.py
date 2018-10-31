#encoding:utf-8

import socket


#洪水攻击，通过伪造IP地址头，发起大量的请求，造成服务无法承载，
"""
A 访问 B机器需要三次握手，如果没有回复，等待最大时间为默认超时时间，超过默认时间，自动关闭；
建立一个连接通过IP地址加端口
"""

s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
s.bind(8888)
s.listen(10)
conn,recv = s.connect()