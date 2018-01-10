
# queue队列

import queue

# q = queue.Queue()
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())
# # block参数指定是否阻塞
# # print(q.get(block=False))  # raise Empty
# # q.get_nowait()  # raise Empty
# q.get()

# # maxsize设置列表长度
# q = queue.Queue(maxsize=2)
# q.put(1)
# # q.get_nowait()
# q.put(2)
# q.put(3)

# LIFO 后进先出
# q = queue.LifoQueue()
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())

# Priority 设置取出优先级, 放进去元组(优先级, 值)
q = queue.PriorityQueue()
q.put((1, 'z'))
q.put((2, 'b'))
q.put((-10, 'a'))
q.put((-1, 'c'))
print(q.get())
print(q.get())
print(q.get())
print(q.get())

q.put(('d', 'z'))
q.put(('h', 'b'))
q.put(('g', 'a'))
q.put(('a', 'c'))
print(q.get())
print(q.get())
print(q.get())
print(q.get())

'''
(-10, 'a')
(-1, 'c')
(1, 'z')
(2, 'b')
('a', 'c')
('d', 'z')
('g', 'a')
('h', 'b')
'''
