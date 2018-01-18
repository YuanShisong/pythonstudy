
# 多进程
# import multiprocessing, time, threading
#
#
# def thread_run():
#     print('thread', threading.get_ident())
#
#
# def run(n):
#     time.sleep(1)
#     print('process', n)
#     threading.Thread(target=thread_run).start()
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         p = multiprocessing.Process(target=run, args=(i,))
#         p.start()
#     # p.join()


# from multiprocessing import Process
# import os
#
#
# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process id:', os.getppid())  # 父进程ID
#     print('process id:', os.getpid())  # 子进程ID
#     print('\n\n')
#
#
# def f(name):
#     info(name)
#     print('hello', name)
#
#
# if __name__ == '__main__':
#     info('\033[32;1mmain process line\033[0m')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     # p.join()
