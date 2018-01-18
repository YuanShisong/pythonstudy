
#
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 声明socket类型,同事生成socket连接对象

client.connect(('localhost', 8888))

while True:
    msg = bytes(input('>>:'), encoding='utf-8')
    client.send(msg)
    data = client.recv(1024)
    # data = client.recv(1024)
    print(data)