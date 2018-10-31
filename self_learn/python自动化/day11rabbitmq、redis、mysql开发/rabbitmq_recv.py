#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/27 16:39

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.56.11",port=5672,)) #实例化一个连接，并配置连接的服务端IP和端口
channel = connection.channel() #创建一个连接通道
print(channel)
channel.queue_declare(queue='hello',durable=True) #申明一个hello队列，如果没有则创建,durable=True持久化队列

def callback(channel, method, properties, body):
    print("channel: ",channel)
    print("method: ",method)
    print("properties: ",properties)
    # time.sleep(25)
    channel.basic_ack(delivery_tag=method.delivery_tag) #确认消息已经推送完成，当no_ack=False时需要用到

    print(" [x] Received %r" % body.decode())#body即为收取到的消息内容，二进制

#如果Rabbit只管按顺序把消息发到各个消费者身上，不考虑消费者负载的话，很可能出现，一个机器配置不高的消费者那里堆积了很多消息处理不完，同时配置高的消费者却一直很轻松。
channel.basic_qos(prefetch_count=2)  #为了解决这个问题，配置perfetch=1,意思就是告诉RabbitMQ在我这个消费者当前消息还没处理完的时候就不要再给我发新消息了。
channel.basic_consume(callback,  #如果收到消息就调用callback函数来处理消息
                      queue="hello",
                      no_ack=False) #True不确认消息是否处理完,为Fasle则需要确认消息是否处理完，如果没有处理完就断掉，则再次连上或者其他连接继续处理
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming() #开始收消息，一旦启动永远收取