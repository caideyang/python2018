#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/28 12:06

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="192.168.56.11",
    port=5672
))
channel = connection.channel()
channel.exchange_declare(exchange="direct_logs",
                         exchange_type="direct")
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage:%s [info][warning][error]\n" % sys.argv[0])
    sys.exit()
for severity in severities:
    channel.queue_bind(exchange="direct_logs",
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')
def callback(channel,method,properties,body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
channel.start_consuming()