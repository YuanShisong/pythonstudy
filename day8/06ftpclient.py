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
    local_md5 = hashlib.md5()
    if 'download' == opt:
        length = client.recv(128).decode()  # size of the file
        if 'None' == length:
            print('File does not exist.')
        else:
            client.send(b'Now start sending the file.')  # solve stick package problem
            file_size = int(length)
            # print(file_size)
            recv_size = 0
            file = open(filename + '.new', 'bw')
            while recv_size < file_size:
                data = client.recv(1024)
                file.write(data)
                local_md5.update(data)
                recv_size += len(data)
            else:
                file.close()
                # print(recv_size)  # file size not equal on Windows ??? No, it's because of the stick package problem, cost me one Hour FFF.
                client.send(b'send md5 code in')  # solve stick package problem
                sever_md5 = client.recv(1024).decode()
                if sever_md5 != local_md5.hexdigest():  # check md5 code
                    print('md5 code not equal.')
                else:
                    print('File transfer finished and md5 ok.')

    elif 'upload' == opt:
        pass

client.close()