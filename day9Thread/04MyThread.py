
# 继承threading.Thread类

import threading, time


class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        self.n = n

    def run(self):
        print('task', self.n)
        time.sleep(2)


t1 = MyThread(1)
t2 = MyThread(2)

t1.start()
t2.start()

# 这种方式并没有启动线程依然是单线程
# t1.run()
# t2.run()

# 启动多个线程
def run(n):
    print('task', n)
    time.sleep(2)


for i in range(50):
    t = threading.Thread(target=run, args=(i, ))
    t.start()

