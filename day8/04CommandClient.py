
# 客户端连上服务端后，在客户端输入系统命令，在服务端执行，将执行结果返回给客户端

import socket
client = socket.socket()

client.connect(('localhost', 9999))

while True:
    cmd = input('>>:').strip()
    if not cmd:
        print('can not input blank.')
        continue
    client.send(cmd.encode())

    length = client.recv(128).decode()  # length of the outcome
    print(length)

    out_come = ''

    while len(out_come) < int(length):
        # print('-------------')
        out_come += client.recv(8*4*10).decode()
    else:
        print('command has no outcome.')
    print(out_come)
    

client.close()
