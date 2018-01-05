
import socket
# server = socket.socket()
# server.bind(('127.0.0.1', 9999))
# server.listen()
# print('before accept')
# soc, addr = server.accept()
# print('after accept')
# data = server.recv(1024)
# print('recv:', data)
# server.send(data.upper())
# server.close()

# server = socket.socket()
# server.bind(('127.0.0.1', 9999))
# server.listen()
# sock, addr = server.accept()
# print(sock, addr)
# data = sock.recv(1024)
# print('recv:', data)
# sock.send(data.upper())
# server.close()

server = socket.socket()
server.bind(('127.0.0.1', 9999))
server.listen()
while True:
    sock, addr = server.accept()
    data = sock.recv(1024)
    print('recv:', data)
    if data == b'quit':
        break
    sock.send(data.upper())
server.close()
print('server close')
