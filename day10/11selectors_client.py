#_*_coding:utf-8_*_


import socket
import sys

messages = [ b'Message1',
             b'Message2',
             b'Message3',
             ]
server_address = ('192,168.212.180', 9999)


# Create a TCP/IP socket
socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(5)]

# Connect the socket to the port where the server is listening
print('connecting to %s port %s' % server_address)
for s in socks:
    s.connect(server_address)

for message in messages:

    # Send messages on both sockets
    for s in socks:
        # print('%s: sending "%s"' % (s.getsockname(), message) )
        s.send(message)

    # Read responses on both sockets
    for s in socks:
        data = s.recv(1024)
        print( '%s: received "%s"' % (s.getsockname(), data) )
        if not data:
            print(sys.stderr, 'closing socket', s.getsockname() )
