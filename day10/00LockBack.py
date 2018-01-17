
# 线程 进程

# 线程共享内存
# 加锁    mutex互斥锁
#        递归锁
# join() 等待执行结果后
# 守护线程
# 队列queue：(Java中有)
#       解耦
#       提高处理效率
#         FIFO
#         LIFO
#       生产者消费者模式
# event

# if True:
#     i = 1
# print(i)  # 1
#
if False:
    i = 1
print(i)  # NameError: name 'i' is not defined


# python 的多线程不适合cpu密集操作型的任务，适合IO操作密集型的任务
