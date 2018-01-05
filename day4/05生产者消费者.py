# 生产者消费者模型
# 1、

import time
# def customer(name):
#     print('customer %s is ready.' %name)
#     while True:
#         food = yield
#         print('%s ate %s.' %(name,food))
#
# def producer(name, food, cust):
#     print('%s Begin produce %s' %(name,food))
#     cust.__next__()
#     while True:
#         time.sleep(1)
#         print('%s\'s %s is ready!!!' % (name, food))
#         cust.send(food)
# c1 = customer('Joshua')
# c2 = customer('Joey')
# producer('Joshua', 'steak', c1)
# producer('Joshua', 'steak', c2)

'''
Joshua Begin produce steak
customer Joshua is ready.
Joshua ate steak.
Joshua ate steak.
Joshua ate steak.
Joshua ate steak.
.......
'''

# 2、以上方式,一个生产者和一个消费者一一绑定,Joey没有得到任何食物，生产者生产多少，消费者就消费多少，像大鸟养了一只喂不饱的小鸟。不符合实际情况
# 如果大鸟养了多只小鸟呢，需要把食物平均分配给多只小鸟怎么办


def customer(name):
    print('customer %s is ready.' % name)
    while True:
        food = yield
        print('%s ate %s.' % (name, food))


def producer(name, food, cust):
    print('%s Begin produce %s' % (name, food))
    time.sleep(1)
    cust.send(food)


c1 = customer('Joshua')
c2 = customer('Joey')
c3 = customer('Monica')
c1.__next__()
c3.__next__()
c2.__next__()

for i in range(9):
    if i % 3 == 0:
        producer('Joshua', 'steak', c1)
    elif i % 3 == 1:
        producer('Joshua', 'steak', c2)
    else:
        producer('Joshua', 'steak', c3)
