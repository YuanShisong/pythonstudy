'''
+------------+
| BaseServer |
+------------+
      |
      v
+-----------+        +------------------+
| TCPServer |------->| UnixStreamServer |
+-----------+        +------------------+
      |
      v
+-----------+        +--------------------+
| UDPServer |------->| UnixDatagramServer |
+-----------+        +--------------------+

Creating a server requires several steps.
    First, you must create a request handler class by subclassing the BaseRequestHandler class and overriding its handle() method; this method will process incoming requests.
        继承BaseRequestHandler以创建请求处理类，并重写handle()方法，此方法中处理请求
    Second, you must instantiate one of the server classes, passing it the server’s address and the request handler class.
        实例化server class中的一个，将IP地址和request handler class传递给实例
    Then call the handle_request() or serve_forever() method of the server object to process one or many requests.
        然后调用handle_request()或serve_forever()方法，处理一个或多个请求
    Finally, call server_close() to close the socket.
        最终调用server_close()关闭socket
'''

import socketserver

class MyRequestHandler(socketserver.BaseRequestHandler):
    '''
        My RequestHandler 自定义RequestHandler
        MyRequestHandler will be instantiated on every request.
    '''
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print('{} wrote:'.format(self.client_address))
                print(self.data)
                self.request.sendall(self.data.upper())
            except ConnectionResetError as e:
                print('error:', e)
                break
print(__name__)

if __name__ == '__main__':
    HOST, PORT = 'localhost', 9999
    # server = socketserver.TCPServer((HOST, PORT), MyRequestHandler)  # singleton 单线程
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyRequestHandler)  # multithreading 多线程
    # server = socketserver.ForkingTCPServer((HOST, PORT), MyRequestHandler)  #  multiprocess 多进程
    # AttributeError: module 'socketserver' has no attribute 'ForkingTCPServer'
    server.serve_forever()
