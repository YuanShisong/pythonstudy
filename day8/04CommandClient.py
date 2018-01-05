
# 客户端连上服务端后，在客户端输入系统命令，在服务端执行，将执行结果返回给客户端

import socket
client = socket.socket()

client.connect(('localhost', 9999))

while True:
    cmd = input('>>:').strip()
    if not cmd:
        print('不能输入空')
        continue
    client.send(cmd.encode())

    res = client.recv(1024).decode()

    print(res)
    

client.close()