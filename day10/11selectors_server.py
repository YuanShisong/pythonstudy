
# selectors 模块的用法


import selectors, socket

sel = selectors.DefaultSelector()


def read(conn, mask):
    data = conn.recv(1024)
    if data:
        # print('echoing', repr(data), 'to', conn)
        conn.send(data)
    else:
        # print('closing', conn)
        sel.unregister(conn)
        conn.close()


def accept(sock, mask):
    '''
    接收新连接
    :param sock: 被监听socket，即server自己
    :param mask:
    :return:
    '''
    conn, addr = sock.accept()  # conn为新连接
    # print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)  # 监听新连接的READ事件，注册回调函数read处理read事件


socket = socket.socket()
socket.bind(('localhost', 9999))
socket.listen(100)
socket.setblocking(False)  # 设置非阻塞
sel.register(socket, selectors.EVENT_READ, accept)  # 监听socket的READ事件，事件触发说明有新连接进入，注册回调函数accept处理新连接

while True:
    event = sel.select()
    for key, mask in event:
        # print(key)  # SelectorKey(fileobj=<socket.socket fd=240, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9999)>, fd=240, events=1, data=<function accept at 0x000000000255DD90>)
        # print(mask)
        callback = key.data  # 注册的回调函数: data=<function accept at 0x000000000255DD90>
        callback(key.fileobj, mask)  # key.fileobj是文件句柄
        # mask是key的events值,即事件类型：EVENT_READ=(1<<0) EVENT_WRITE=(1<<1)
