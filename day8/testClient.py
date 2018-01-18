import socket
client = socket.socket()

client.connect(('localhost', 9999))

res = client.recv(1024).decode()
print(res)

res = client.recv(1024).decode()
print(res)

res = client.recv(1024).decode()
print(res)

res = client.recv(1024).decode()
print(res)

res = client.recv(1024).decode()
print(res)

res = client.recv(1024).decode()
print(res)
