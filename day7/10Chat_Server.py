
# 聊天室服务端
'''
需求：
    服务端开启服务后，允许多个客户端同时连接
    客户端上线，给所有在线客户端推送上线提醒
    客户端发文字，服务端将客户端名称和所发内容推送给所有在线客户端
'''

import socket

server = socket.socket()  # 生成socket对象

server.bind(('localhost', 9999))  # 绑定IP地址

# Enable a server to accept connections.
server.listen(1)  # 最多允许三个等待链接的请求 backlog:积压,存货
# D:\999-Personal\Python\study\day7>python 11Chat_Client1.py
# Traceback (most recent call last):
#   File "11Chat_Client1.py", line 8, in <module>
#     conn = client.connect(('127.0.0.1', 9999))  # 连接到服务
# ConnectionRefusedError: [WinError 10061] 由于目标计算机积极拒绝，无法连接。
while True:
    # Wait for an incoming connection.  Return a new socket representing the connection, and the address of the client.
    sock, addr = server.accept()
    print(addr, '上线')
    while True:
        try:
            data = sock.recv(10).strip()
            if not data:
                print(addr, 'is OFF')
                break
            else:
                print('%s says: \n \t %s' % (addr, data.decode()))
        except ConnectionResetError:
            print(addr, '下线')
            break

# sock.send(b'321')
server.close()


