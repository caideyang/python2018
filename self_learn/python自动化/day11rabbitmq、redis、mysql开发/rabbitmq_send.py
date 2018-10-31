#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/27 16:17

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.56.11",port=5672,)) #实例化一个连接，并配置连接的服务端IP和端口
channel = connection.channel() #创建一个连接通道
channel.queue_declare(queue='hello',durable=True) #申明一个hello队列，如果没有则创建,durable=True持久化队列，即即使rabbitmq重启，队列依然存在
while True:
    data = input(">>>")
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=data,
                          properties=pika.BasicProperties(
                              delivery_mode=2, #使消息持久化，即即使rabbitmq重启，消息依然存在
                          ))
    print(channel)
    print("Send  %s" % data)

connection.close()