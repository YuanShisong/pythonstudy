
# 客户端下载文件需求
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
        server_md5 = hashlib.md5()
        if 'download' == cmd:
            if os.path.exists(filename):
                file = open(filename, 'rb')
                file_size = os.stat(filename).st_size
                conn.send(str(file_size).encode())  # send file size
                # conn.recv(1024)  # wait for ack
                for line in file:
                    server_md5.update(line)
                    conn.send(line)
                else:
                    file.close()
                    # conn.recv(1024)
                    conn.send(server_md5.hexdigest().encode())
            else:
                conn.send(b'None')  # send file size
                # conn.recv(1024)  # wait for ack
        elif 'upload' == cmd:
            length = conn.recv(128).decode()  # size of the file
            # conn.send(b'Now start sending the file.')  # solve stick package problem
            file_size = int(length)
            recv_size = 0
            file = open(filename + '.upload', 'bw')
            while recv_size < file_size:
                size = 0  # new way of solving stick package problem
                if file_size - recv_size < 1024:
                    size = file_size - recv_size  # receive no matter how much left when it's less then 1024 bytes
                else:
                    size = 1024
                data = conn.recv(size)
                file.write(data)
                server_md5.update(data)
                recv_size += len(data)
            else:
                file.close()
                # conn.send(b'send md5 code in')  # solve stick package problem
                client_md5 = conn.recv(1024).decode()
                print(server_md5.hexdigest())
                if client_md5 != server_md5.hexdigest():  # check md5 code
                    print('md5 code not equal.')
                    conn.send(b'fail')
                else:
                    print('File transfer finished and md5 ok.')
                    conn.send(b'ok')
server.close()