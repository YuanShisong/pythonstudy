
# 静态方法
# class People(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @staticmethod  # 静态方法
#     def speak(obj):
#         print('%s:blah blah blah' %obj.name)
#
# p = People("Joshua", 29)
# p.speak(p)
#
# g = People("Emily", 29)
#
# People.speak(g)

# 类方法 只能访问类变量，不能访问实例变量
# class People(object):
#     name = "Emily"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod  # 类方法 只能访问类变量，不能访问实例变量
#     def speak(self):
#         print('%s:blah blah blah' %self.name)
#
# p = People('Joshua', 29)
# p.speak()  # Emily:blah blah blah
# People.speak()  # Emily:blah blah blah


# # 私有属性 属性方法 对应Java中 getter setter方法
# class People(object):
#     '''类：People'''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__food = None
#
#     @property  # 属性方法
#     def speak(self):
#         print('%s:blah blah blah' %(self.name))
#
#     @property  # 带参数的属性方法
#     def eat(self):
#         print('%s eats %s' % (self.name, self.__food))
#
#     @eat.setter  # 属性方法的setter方法,可以不同名,但调用方式就发生改变了
#     def eatsetter(self, food):
#         print('eat.setter:', food)
#         self.__food = food
#     #同名setter方法
#     @eat.setter  # 属性方法的setter方法
#     def eat(self, food):
#         print('eat.setter:', food)
#         self.__food = food
#
#     # 删除私有属性
#     @eat.deleter
#     def eat(self):
#         del self.__food
#         print('deleter done.')
#
#     # def test(self):
#     #     print('method test')
#     #
#     # @test.setter  # AttributeError: 'function' object has no attribute 'setter' 普通方法没有setter属性
#     # def testsetter(self):
#     #     print('test.setter')
#
# p = People('Joshua', 29)
# People.speak  # 结果为空 调不到属性方法
# People.eat  # 结果为空 调不到属性方法
# p.speak()  # 'NoneType' object is not callable
# p.speak  # Joshua:blah blah blah
# p.eat  # eat() missing 1 required positional argument: 'argv'
# p.eat = '包子'  # can't set attribute
# p.eatsetter = '包子'  # eat.setter: 包子
# p.testsetter = 'test'  # AttributeError: 'function' object has no attribute 'setter'
# p.eat = '牛排'
# p.eat

# 删除私有属性
# del p.eat  # AttributeError: can't delete attribute
# del p.eat  # deleter done.
# p.eat  # AttributeError: _People__food