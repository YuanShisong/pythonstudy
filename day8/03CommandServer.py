
# 客户端连上服务端后，在客户端输入系统命令，在服务端执行，将执行结果返回给客户端

import socket, os
server = socket.socket()

server.bind(('localhost', 9999))

server.listen()

while True:
    conn, addr = server.accept()

    while True:
        data = conn.recv(1024).strip()

        if not data:
            print('client is off')
            break

        res = os.popen(data.decode()).read()

        if not res:
            conn.send('命令无返回结果'.encode())
        conn.send(res.encode())

server.close()