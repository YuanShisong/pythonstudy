'''
# 知识点回顾 socked编程步骤
1、引入socket包
2、服务端
    1)创建socket对象
    2)bind绑定IP地址和端口
    3)listen监听端口
    4)accept等待客户端连接,处于阻塞状态,返回connection 和 客户端地址
3、客户端
    1)创建socket对象
    2)bind绑定IP地址和端口
    3)send向服务端发送信息
    4)recv从服务端接收信息
'''

# 客户端连上服务端后，在客户端输入系统命令，在服务端执行，将执行结果返回给客户端

import socket, os
server = socket.socket()

server.bind(('localhost', 9999))

server.listen()

while True:
    conn, address = server.accept()

    while True:
        data = conn.recv(128).strip()

        if not data:
            print('client is off')
            break

        res = os.popen(data.decode()).read()

        conn.send(str(len(res.encode())).encode())
        confirm = conn.recv(1024)  # 接收服务端确认信息,解决粘包问题
        conn.send(res.encode())

server.close()
