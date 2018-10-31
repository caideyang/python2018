#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/10/30 13:32

from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['<h1>Hello, 路飞学成!</h1>'.encode('gbk'), '<h2>你好</h2>'.encode('gbk')]

httpd = make_server('', 8080, application)

print('Serving HTTP on port 8080...')
# 开始监听HTTP请求:
httpd.serve_forever()