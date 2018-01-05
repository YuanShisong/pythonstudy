
#
import socket

# client = socket.socket()  # 声明socket类型,同时生成socket连接对象
# client.connect(('127.0.0.1', 9999))
# # client.send('Hello World')  # TypeError: a bytes-like object is required, not 'str'
# # python3中必须发送byte类型
# client.send(b'Hello World')
# data = client.recv(1024)
# print('recv:', data)

client = socket.socket()  # 声明socket类型,同事生成socket连接对象
client.connect(('127.0.0.1', 9999))
client.send(b'Hello World')
data = client.recv(1024)
print('recv:', data)


# client = socket.socket()  # 声明socket类型,同事生成socket连接对象
# client.connect(('127.0.0.1', 9999))
# client.send('你好 1'.encode())
# data = client.recv(1024)
# print('recv:', data.decode())
#
# client = socket.socket()  # 声明socket类型,同事生成socket连接对象
# client.connect(('127.0.0.1', 9999))
# client.send(b'quit')
# data = client.recv(1024)
# print('recv:', data)
