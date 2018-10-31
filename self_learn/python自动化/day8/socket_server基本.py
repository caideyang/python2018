#encoding:utf-8

import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print("客户端IP：{}，端口:{} 连接成功".format(self.client_address[0],self.client_address[1]))
        while True:
            try: #使用try except捕捉客户端连接断开异常
                self.data = self.request.recv(1024).strip()
                print("{} 端口wrote:".format(self.client_address[1]))
                print(self.data)
                if not self.data:
                    print(self.client_address, "断开")
                    break
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("error:" ,e,"客户端IP：{}，端口:{} 连接断开".format(self.client_address[0],self.client_address[1]))
                break

if __name__ == "__main__":
    HOST,PORT = "localhost",9999

    # server = socketserver.TCPServer((HOST,PORT),MyTCPHandler)  #只支持单个客户端连接
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler) #多并发连接支持
    server.serve_forever()