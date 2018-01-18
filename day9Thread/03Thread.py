
# 最简单的多线程
# Thread module emulating a subset of Java's threading model.
import threading, time


def run(n):
    print('task', n)
    time.sleep(2)


t1 = threading.Thread(target=run, args=('1',))
t2 = threading.Thread(target=run, args=('1',))

t1.start()
t2.start()