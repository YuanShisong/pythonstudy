
#

import threading, time


num = 0
lock = threading.Lock()


def run(n):
    # lock.acquire()
    global num
    # time.sleep(0.00001)
    num += 1
    print(num)
    # lock.release()


for i in range(10000):
    t = threading.Thread(target=run, args=(i, ))
    t.start()

# time.sleep(10)

# print(num)


# 试了半天Python就没有线程安全问题， 不管3.6还是2.7
