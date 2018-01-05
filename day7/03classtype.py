
#
# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print('My name is %s' %self.name)
#
# f = Foo('Joshua')
# f.talk()
#
# print(f)  # <__main__.Foo object at 0x00000000024582E8>
# print(Foo)  # <class '__main__.Foo'>
# print(type(f))  # <class '__main__.Foo'>
# print(type(Foo))  # <class 'type'>

# 反射方式创建类
def func(self):
    print('Hello world.')

Foo = type('Foo', (), {'talk':func})

# f = Foo
# print(type(Foo))  # <class 'type'>
# f.talk()  # TypeError: func() missing 1 required positional argument: 'self'
# f.func()  # AttributeError: type object 'Foo' has no attribute 'func'
# f.talk(f)  # Hello world.

# f = Foo()
# print(type(Foo))  # <class 'type'>
# f.talk()  # Hello world.
# f.func()  # AttributeError: 'Foo' object has no attribute 'func'
# f.talk(f)  # TypeError: func() takes 1 positional argument but 2 were given

def func(self):
    print('Hello %s.' %self.name)

def __init__(self, name, age):
    self.name = name
    self.age = age

Foo = type('Foo', (object,), {'talk':func, '__init__':__init__})
# Foo = type('Foo', (object), {'talk':func, '__init__':__init__})  # TypeError: type.__new__() argument 2 must be tuple, not type

print(Foo.mro())  # [<class '__main__.Foo'>, <class 'object'>]

f = Foo('Joshua', 29)
f.talk()