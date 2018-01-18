
# Join 等待线程执行完毕后再往下执行
import threading, time

start = time.time()


def run(n):
    # print('Thread', n)
    time.sleep(2)
    # print('Thread %s done.' % n)
    # pass


t1 = threading.Thread(target=run, args=(1, ))
t2 = threading.Thread(target=run, args=(2, ))

# ---以下代码将两个线程变为串行执行：启动一个线程Join一个线程---
# t1.start()
# t1.join()  # 等待线程执行完毕
# t2.start()
# t2.join()
# print('Main Thread.')
# It takes 4.0012288093566895 seconds.

# ---以下代码将两个线程变为串行执行:两个线程一起启动后,两个线程一起Join---
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('Main Thread.')
# It takes 2.0001144409179688 seconds.

# # 多个线程计时
# threads = []
# for i in range(500):  # 启动单个进程用时大概0.1ms
#     t = threading.Thread(target=run, args=(i,))
#     t.start()
#     threads.append(t)
#
# print('Main Thread.', threading.current_thread(), threading.active_count())
# for t in threads:
#     t.join()
# end = time.time()
# print('It takes %s seconds.' % (end - start))


