#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/28 22:40
import uuid,pika
import time

class FibonacciRpcClient():
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host="192.168.56.11",
            port=5672
        ))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response,
                                   no_ack=True,
                                   queue=self.callback_queue)
    def on_response(self,channel,method,props,body):  #回调函数
        if self.corr_id == props.correlation_id: #判断程序生成的uuid与rpcServer回调回来的uuid是否相等
            self.response = body  #相等，则将回调回来的body赋给self.response
    def call(self,num): #执行方法
        self.response = None
        self.corr_id = str(uuid.uuid4()) #生成uuid编号
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id
                                   ),
                                   body=str(num))
        while self.response is None: #当self.response未返回数据,一直启动一个事件进行阻塞
            time.sleep(0.5)
            print("No db received...")
            self.connection.process_data_events()
        return int(self.response) #返回获取到的值



if __name__ == "__main__":
    fibonacci_rpc = FibonacciRpcClient()
    while True:
        num = int(input("Your number>>>").strip())
        print("[X] Requesting fib(%s)" %num)
        response = fibonacci_rpc.call(num)
        print("[.]Got %r" %response)
