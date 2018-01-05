
#

import socket

client = socket.socket()  # 创建socket对象

conn = client.connect(('127.0.0.1', 9999))  # 连接到服务

# client.send(b'123')  # 发送内容
# data = client.recv(1024)
# print(data)
while True:
    con = input('>>:').strip()
    if con == 'quit':
        client.close()
        break
    elif con == '':
        print('不能发送空字符串')
    else:
        client.send(con.encode())
