
from multiprocessing import Process, Queue
import threading

# #进程间通信
# 1、进程Queue
# def f(q):
#     q.put('123')
#
#
# if __name__ == '__main__':
#     q = Queue()
#     Process(target=f, args=(q,)).start()
#     print(q.get())  # 123


# def foo():
#     q.put('123')  # NameError: name 'q' is not defined
#
#
# if __name__ == '__main__':
#     q = Queue()
#     #子进程访问不到父进程中的q
#     Process(target=foo).start()  #
#     print(q.get())
#
#     # 子线程能访问到父线程中的q
#     threading.Thread(target=foo, ).start()
#     print(q.get())  # 123

#
# def bar(q):
#     q.put('123')  # NameError: name 'q' is not defined
#
#
# if __name__ == '__main__':
#     q = Queue()
#     Process(target=bar, args=(q,)).start()
#     print(q.get())


# 通过pipe通信
from multiprocessing import Pipe


def f(conn):
    conn.send('from child')
    print(conn.recv())


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()  # 管道两端
    Process(target=f, args=(child_conn,)).start()
    print(parent_conn.recv())
    parent_conn.send('from parent')
    parent_conn.recv()

