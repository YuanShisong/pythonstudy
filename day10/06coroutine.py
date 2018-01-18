
# 协程
# 协程拥有自己的寄存器上下文和栈
# 协程的好处：
#     无需线程上下文切换的开销
#     无需原子操作锁定及同步的开销
#           "原子操作(atomic operation)是不需要synchronized"，所谓原子操作是指不会被线程调度机制打断的操作；这种操作一旦开始，就一直运行到结束，中间不会有任何 context switch （切换到另一个线程）。
#           原子操作可以是一个步骤，也可以是多个操作步骤，但是其顺序是不可以被打乱，或者切割掉只执行部分。视作整体是原子性的核心。
#     方便切换控制流，简化编程模型
#     高并发+高扩展性+低成本：一个CPU支持上万的协程都不是问题。所以很适合用于高并发处理
#
# 缺点：
#     无法利用多核资源：协程的本质是个单线程,它不能同时将单个CPU的多个核用上,协程需要和进程配合才能运行在多CPU上.当然我们日常所编写的绝大部分应用都没有这个必要，除非是cpu密集型应用。
#     进行阻塞（Blocking）操作（如IO时）会阻塞掉整个程序

# python 的yield就支持协程但支持不完全，见之前生产者消费者模式

# import time
#
#
# def consumer(name):
#     '''
#     消费者
#     :param name: 名字
#     :return: 无返回值
#     '''
#     while True:
#         baozi = yield
#         print('[%s] is eating baozi:[%s]' %(name, baozi))
#
#
# def producer():
#     r1 = con1.__next__()
#     r2 = con2.__next__()
#     print(r1)
#     print(r2)
#     n = 0
#     while n < 5:
#         n += 1
#         print("\033[32;1m[producer]\033[0m is making baozi %s" % n)
#         con1.send(n)
#         con2.send(n)
#         time.sleep(0.5)
#     pass
#
#
# if __name__ == '__main__':
#     con1 = consumer('c1')
#     con2 = consumer('c2')
#     p = producer()

# greenlet 是封装好的协程
# from greenlet import greenlet
#
#
# def test1():
#     print(1)
#     g2.switch()
#     print(2)
#     g2.switch()
#     pass
#
#
# def test2():
#     print(3)
#     g1.switch()
#     print(4)
#     pass
#
#
# g1 = greenlet(test1)  # 启动一个协程 指向test1方法
# g2 = greenlet(test2)
# g1.switch()  # 1 3 2 4
# g2.switch()  # 3 1 4


# gevent 对greenlet进行了封装
# windows上安装失败，以下代码在ubuntu上执行

import gevent


def func1():
    print('\033[31;1m李闯在跟海涛搞...\033[0m')
    gevent.sleep(2)
    print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')


def func2():
    print('\033[32;1m李闯切换到了跟海龙搞...\033[0m')
    gevent.sleep(1)
    print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m')


def func3():
    print('\033[33;1m3...\033[0m')
    gevent.sleep(1)
    print('\033[33;1m李3...\033[0m')


gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    # gevent.spawn(func3),
])
