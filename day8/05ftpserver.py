
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


def get_client_check(conn):
    msg = conn.recv(1024).decode('utf-8')
    conn.send(b'ok')
    return msg


while True:
    conn, address = server.accept()
    while True:
        operation = get_client_check(conn)
        if not operation:
            break
        if b'upload' == operation:
            code = get_client_check(conn)  # receive file's md5 code
            filename = get_client_check(conn)  # file name
            hdl = os.open(filename + '.backup', 'a')  # open file in append mode
            length = int(get_client_check(conn))
            count = 0
            while count < length:
                data = conn.recv(1024)
                count += len(data)
                hdl.write(data)
            hdl.close()
        elif b'download' == operation:
            pass


server.close()


''' 
----上传下载功能----
客户端输入操作类型(download, upload)
服务端响应,反馈服务端准备好了
客户端接收到服务端响应,要求用户输入要上传或下载的文件名
上传
    客户端检查文件是否存在
    计算文件md5值
    将md5值发送给服务端
    客户端发送文件
    服务端接收文件
    服务端计算接收到文件的md5值，判断文件是否完整
    服务端给客户端反馈
下载
    服务端检查文件是否存在
    计算文件md5值
    将md5值发送给客户端
    服务端发送文件
    客户端接收文件
    客户端计算接收到文件的md5值，判断文件是否完整
    客户端给客户端反馈
'''