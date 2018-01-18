
# 用select实现socket server
import select
import socket
import queue

server = socket.socket()
server.bind(('localhost', 8888))
server.listen(100)

server.setblocking(False)


msg_dic = {}
inputs = [server, ]  # select监控列表, 第一个是server自己, 如果server有请求说明有新连接进来，
outputs = []
while 1:
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    # readable, writeable, exceptional和三个参数有序对应，包含已READY状态的文件描述符的子集
    # inputs, outputs, inputs

    # *** 要从客户端读数据就往inputs中添加要读取的目标连接 ***
    # *** 要往客户端写数据就往outputs中添加要写的目标连接 ***

    # The return value is a tuple of three lists corresponding to the first three
    # arguments; each contains the subset of the corresponding file descriptors
    # that are ready.
    #
    # *** IMPORTANT NOTICE *** windows平台上只支持sockets类型文件描述符，Unix平台上支持所有类型文件描述符
    # On Windows, only sockets are supported; on Unix, all file descriptors can be used.

    # 处理读
    for r in readable:
        if r is server:  # 代表进来一个新连接
            conn, addr = server.accept()
            # print(conn.recv(1024))  # BlockingIOError: [WinError 10035] 无法立即完成一个非阻止性套接字操作。
            # 将连接放到监控列表
            # print('新连接：', conn)
            inputs.append(conn)  # 因为这个新建立的连接还没发数据过来，在非阻塞状态下，程序会报错
            #所以要想实现这个客户端发数据过来时server能知道，就需要让select再监控这个连接
            msg_dic[conn] = queue.Queue()  # 初始化一个队列，后面存要返回给这个客户端的数据
        else:  # 代表其他被监控连接有数据进来
            data = r.recv(1024)
            # print('收到数据：', data)
            msg_dic[r].put(data)
            outputs.append(r)  # 放入返回的连接队列里
            # outputs.append(r)  # 放入返回的连接队列里
            # r.send(data)

    # print(readable, writeable)
    # 处理写
    for w in writeable:  # 要返回给客户端的连接列表
        data_to_client = msg_dic[w].get()
        w.send(data_to_client)
        outputs.remove(w)

    # 处理异常
    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)

        del msg_dic[e]
