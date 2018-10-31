#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/28 11:19

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="192.168.56.11",
    port=5672
))
channel = connection.channel()
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
while True:
    message = input(">>>").strip()
    message = ''.join(sys.argv[1:]) or message
    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body=message)
    print("Send %r" %message)
connection.close()


#
# if __name__ == "__main__":
#     pass