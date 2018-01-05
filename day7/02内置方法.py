
# 内置方法
# __doc__
class People(object):
    '''类：People'''
    a = []
    b = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.data = {}

    def __call__(self, *args, **kwargs):
        '''内置方法：__call__'''
        print("__call__ method")
    def __str__(self):
        print('__str__相当于Java toString()')

    def __setitem__(self, key, value):
        print('__setitem__ %s:%s' %(key,value))
        self.data[key] = value

    def __getitem__(self, item):
        print('__getitem__:%s' %item)
        return self.data[item]

    def __delitem__(self, key):
        print('__delitem__:%s' %key)

p = People('Joshua', 29)
# print(p.__doc__)  # 类：People

# __module__ 输出类所在包路径
# __class__ 输出类型和类全限定名
# from lib.a import C
# obj = C()
# print(obj.__module__)  # lib.a
# print(obj.__class__)  # <class 'lib.a.C'>

# __call__ 调用对象时执行
# p()  # __call__ method
# print(p.__call__.__doc__)  # 内置方法：__call__


# __dict__
# print(People.__dict__)  # {'__module__': '__main__', '__doc__': '类：People', '__call__': <function People.__call__ at 0x0000000001EA9048>, '__dict__': <attribute '__dict__' of 'People' objects>, '__weakref__': <attribute '__weakref__' of 'People' objects>}
print(p.__dict__)  # {'name': 'Joshua', 'age': 29, 'data': {}} __init__构造函数中的参数
# print(('a', 'b').__dict__)  # AttributeError: 'tuple' object has no attribute '__dict__'
# print(1.__dict__)  # NameError: name 'a' is not defined SyntaxError: invalid syntax
# print([].__dict__)  # AttributeError: 'list' object has no attribute '__dict__'

# __str__ 相当于toString
# p.__str__()  # __str__相当于Java toString()

# __setitem__
# __getitem__
# __delitem__
p.__setitem__('weight', 67)
p.__setitem__('height', 172)
print(p.__getitem__('weight'))
print(p.__getitem__('height'))
# p.__delitem__('weight')
# p['weight'] = 70  # __setitem__ weight:70
# print(p['weight'])
# __getitem__:weight
# 70
# del p['weight']  # __delitem__:weight
