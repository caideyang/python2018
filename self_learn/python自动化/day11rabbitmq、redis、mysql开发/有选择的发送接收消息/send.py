#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/28 12:07

import pika,sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="192.168.56.11",
    port=5672
))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) >1 else 'info'
message = ''.join(sys.argv[2:]) or input(">>>")

channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print("Send %r:%r" %(severity,message))
