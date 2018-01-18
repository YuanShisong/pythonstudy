import socket, hashlib, os
client = socket.socket()
client.connect(('localhost', 9999))
while True:
    cmd = input('>>:').strip()  # input operation and filename like 'download test.txt'
    if not cmd:
        print('can not input blank.')
        continue
    client.send(cmd.encode())
    opt, filename = cmd.split(' ')
    client_md5 = hashlib.md5()
    if 'download' == opt:
        length = client.recv(128).decode()  # size of the file
        if 'None' == length:
            print('File does not exist.')
        else:
            # client.send(b'Now start sending the file.')  # solve stick package problem
            file_size = int(length)
            # print(file_size)
            recv_size = 0
            file = open(filename + '.download', 'bw')
            while recv_size < file_size:
                size = 0  # new way of solving stick package problem
                if file_size - recv_size < 1024:
                    size = file_size - recv_size  # receive no matter how much left when it's less then 1024 bytes
                else:
                    size = 1024
                data = client.recv(size)
                file.write(data)
                client_md5.update(data)
                recv_size += len(data)
            else:
                file.close()
                # print(recv_size)  # file size not equal on Windows ??? No, it's because of the stick package problem, No wander always 32 bytes more it's md5 code sticking on tail. Cost me one Hour FFF.
                # client.send(b'send md5 code in')  # solve stick package problem
                sever_md5 = client.recv(1024).decode()
                print(client_md5.hexdigest())
                if sever_md5 != client_md5.hexdigest():  # check md5 code
                    print('md5 code not equal.')
                else:
                    print('File transfer finished and md5 ok.')
    elif 'upload' == opt:
        if os.path.exists(filename):
            file = open(filename, 'rb')
            file_size = os.stat(filename).st_size
            client.send(str(file_size).encode())  # send file size
            # client.recv(1024)  # wait for ack
            for line in file:
                client_md5.update(line)
                client.send(line)
            else:
                file.close()
                # client.recv(1024)
                client.send(client_md5.hexdigest().encode())
                msg = client.recv(1024).decode()
                if msg == 'ok':
                    print('Upload OK.')
                else:
                    print('Upload fail.')
        else:
            print(filename, 'does not exist.')
client.close()