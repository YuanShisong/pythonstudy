
# 需求
# 1、读取文件名
# 2、检测文件是否存在
# 3、打开文件
# 4、检测文件大小
# 5、发送文件大小给客户端
# 6、等待客户端确认
# 7、开始边读边发数据
# 8、发送md5

import socket, os, hashlib
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
        cmd, filename = data.decode().split()
        if 'download' == cmd:
            if os.path.exists(filename):
                md5 = hashlib.md5()
                file = open(filename, 'rb')
                file_size = os.stat(filename).st_size
                conn.send(str(file_size).encode())  # send file size
                conn.recv(1024)  # wait for ack
                for line in file:
                    md5.update(line)
                    conn.send(line)
                else:
                    file.close()
                    conn.recv(1024)
                    conn.send(md5.hexdigest().encode())
            else:
                conn.send(b'None')  # send file size
                conn.recv(1024)  # wait for ack
        elif 'upload' == cmd:
            pass

server.close()