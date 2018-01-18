
# 进程池
from multiprocessing import Process, Pool, freeze_support
import time, os


def Foo(i):
    time.sleep(1)
    print(os.getpid(), i)
    return i


def Bar(arg):
    print('-->%s done. pid:%s' % (arg, os.getpid()))  # 父进程调用


if __name__ == '__main__':
    # freeze_support()  # window平台
    pool = Pool(5)
    print('main process id:', os.getpid())
    for i in range(10):
        # pool.apply(func=Foo, args=(i,))  # 串行执行
        # pool.apply_async(func=Foo, args=(i,))  # 异步执行
        pool.apply_async(func=Foo, args=(i,), callback=Bar)  # 回调函数,
    print('end')
    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭
