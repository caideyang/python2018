#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/28 17:36
import pika,sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="192.168.56.11",
    port=5672
))
channel = connection.channel()
channel.exchange_declare(exchange="topic_logs",
                         exchange_type="topic")
while True:
    routing_key = sys.argv[1] if len(sys.argv) >1 else input("routing_key>>>").strip()
    message = "".join(sys.argv[2:]) or input("message>>>")
    channel.basic_publish(exchange="topic_logs",
                          routing_key=routing_key,
                          body=message)
    print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()





# if __name__ == "__main__":
#     pass