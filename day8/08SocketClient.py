import socket
client = socket.socket()  # 声明socket类型,同事生成socket连接对象
client.connect(('127.0.0.1', 9999))
while True:
    msg = input('>>:').strip()
    client.send(msg.encode())
    data = client.recv(1024)
    print('recv:', data)
