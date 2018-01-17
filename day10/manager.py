
#
# A manager object returned by Manager() controls a server process which holds Python objects and allows other processes to manipulate them using proxies.
# A manager returned by Manager() will support types list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value and Array.

# multiprocessing 包下的Manager

from multiprocessing import Process, Manager
import os


def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.23] = None
    d['pid%s' % os.getpid()] = os.getpid()
    l.append(1)
    print(l, d)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()  # 进程间共享字典
        l = manager.list(range(5))  # 进程间共享列表
        p_list=[]
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()
        print(d)
        print(l)
