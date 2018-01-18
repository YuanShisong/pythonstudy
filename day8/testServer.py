import socket, os, time
server = socket.socket()

server.bind(('localhost', 9999))

server.listen()

conn, address = server.accept()
# 粘包
conn.send(b'1')
conn.send(b'2')
time.sleep(0.5)
conn.send(b'3')
time.sleep(0.5)
conn.send(b'4')
time.sleep(0.5)
conn.send(b'5')
time.sleep(0.5)
conn.send(b'6')
time.sleep(0.5)

server.listen()
