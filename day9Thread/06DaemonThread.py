#
# daemon thread 守护线程
# 主进程结束，其守护进程也随之结束

import threading, time

start = time.time()


def run(n):
    print('Thread', n)
    time.sleep(2)
    print('Thread %s done.' % n)
    # pass


threads = []
for i in range(5):  # 启动单个进程用时大概0.1ms
    t = threading.Thread(target=run, args=(i,))
    t.setDaemon(True)  # 设置为_MainThread的守护线程
    t.start()
    threads.append(t)

# print('Main Thread done, takes time: %s s' % (time.time() - start))
# # Main Thread done, takes time: 0.0009999275207519531 s
# # 没有等守护进程结束

# time.sleep(3)
# print('Main Thread done, takes time: %s s' % (time.time() - start))
# # Main Thread done, takes time: 3.001171827316284 s
# # 守护线程正常结束

