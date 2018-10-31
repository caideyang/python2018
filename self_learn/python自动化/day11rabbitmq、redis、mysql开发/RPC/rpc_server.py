#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/28 22:40
import pika
import time
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="192.168.56.11",
    port=5672
))
channel = connection.channel()
channel.queue_declare(queue="rpc_queue")

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def on_request(channel,method,props,body):
    num = int(body)
    print("[.]fib(%s)" % num)
    response = fib(num)

    channel.basic_publish(exchange='',
                          routing_key=props.reply_to,
                          properties=pika.BasicProperties(
                              correlation_id=props.correlation_id
                          ),
                          body=str(response))
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request,queue="rpc_queue")
print("[X] Awaiting RPC requests")
channel.start_consuming()



# if __name__ == "__main__":
#     pass