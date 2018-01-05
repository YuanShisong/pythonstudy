
'''
列表生成式
'''
a = [1, 2, 3]
print(a)

a = [i**i for i in range(11)]
print(a)
'''结果>>:
[1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489, 10000000000]
'''

'''========迭代器=========='''

# 1、可以通过Iterable的iter()方法生成
print('\n--------iter()方法生成迭代器---------')
a = [1, 2, 3]
# print(next(a))  #TypeError: 'list' object is not an iterator
b = iter(a)
print(type(b))  # <class 'list_iterator'>
print(b.__next__())  # 1
print(b.__next__())  # 2


print('\n---------通过列表生成式创建迭代器-------------')
# 2、通过列表生成式创建迭代器
a = (i*2 for i in range(10))
print(a)  # <generator object <genexpr> at 0x0000000002334F10>

print('\n---------迭代器的一些内置方法-------------')
print(a.gi_running)  # 是否运行中
print(a.gi_code)  # <code object <genexpr> at 0x00000000021956F0, file "D:/999-Personal/Python/study/day4/03迭代器生成器.py", line 15>
print(a.gi_frame)  # <frame object at 0x0000000000454A48>
print(a.gi_yieldfrom)  # None
print(a.send)  # <built-in method send of generator object at 0x0000000002194F10>
print(a.__iter__)
a.__next__
print(next(a))
print(next(a))

print('\n--------斐波那契数列---------')
# 3、斐波那契数列 1 1 2 3 5 8 13
def fib(count):
    a, b, n = 1, 1, 0
    while n < count:
        # print(b)
        # c = a + b
        # a = b
        # b = c
        # 等价于下面代码
        a, b = b, a + b
        # t = (a, a + b)
        # a = t[0]
        # b = t[1]
        n += 1

fib(10)

# 4、自定义迭代器 官方文档有写 https://docs.python.org/3.5/library/stdtypes.html?highlight=iterator#iterator-types
# 为什么官方文档少一个__init__方法呢

print('\n------自定义迭代器-------')
class A:
    def __iter__(self):
        return B()

class B:
    def __init__(self):
        self.start=-1
    def __next__(self):
        self.start +=2
        if self.start >10:
            raise StopIteration
        return self.start

I = A()
for i in I:
    print(i)

class B:
    def __iter__(self):
        return self
    def __init__(self):
        self.start=-1
    def __next__(self):
        self.start +=2
        if self.start >10:
            raise StopIteration
        return self.start
for i in B():
    print(i)

# 3、创建斐波那契数列生成器
# 135301852344706746049 这个数是斐波那契数列的第多少位 写出前边所有位
print('\n------yield-------')
def fib(count):
    a, b, n = 1, 1, 0
    while n < count:
        yield b
        a, b = b, a + b
        n += 1
gen = fib(3)

print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
# print(gen.__next__())  # print(gen.__next__()) StopIteration


# 4、生产者消费者
print('\n--------生产者消费者---------------')

def consumer(name):
    print('%s is ready.' %name)
    while True:
        thing = yield
        print(thing, 'Delicious!!!')

con = consumer('Joshua');
next(con)             # 如果不加这一句,则会报如下错误
con.send('M12 和牛')  # TypeError: can't send non-None value to a just-started generator
con.send('M12 和牛')  # TypeError: can't send non-None value to a just-started generator
con.send('M12 和牛')  # TypeError: can't send non-None value to a just-started generator
con.send('M12 和牛')  # TypeError: can't send non-None value to a just-started generator













# 斐波那契数列生成器
def fib(count):
    a, b, n = 0, 1, 0
    while count > n:
        yield b
        a, b = b, a + b
        n += 1

f = fib(6)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
# print(next(f))
print(f)
