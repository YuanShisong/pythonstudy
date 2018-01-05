
# yield关键字
a = (i**3 for i in range(4))
print(type(a))  # <class 'generator'>

def gen():
    for i in range(4):
        yield i**2
print(gen)  # <function gen at 0x0000000001EC4B70>
mygen = gen()
print(mygen)  # <generator object gen at 0x0000000001E34FC0>

print('\n------------')
def func():
    for i in range(4):
        i**2
print(func)  # <function func at 0x0000000002208048>
f = func()
print(f)

print('\n---------------')
# send
def gen():
    for i in range(4):
        i = yield
        print('i:', i**2)

g = gen()
print(next(g))
g.send(1)
g.send(2)
g.send(3)