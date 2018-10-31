#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/28 11:19

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.56.11',
    port=5672
))
channel = connection.channel()
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs',
                   queue=queue_name)
print("Waiting for logs. To exit press CTRL+C")

def callback(channel,method,properties,body):
    print("Recieved :%r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
channel.start_consuming()