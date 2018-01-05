
# 多继承时父类构造方法执行顺序
class LivingThing(object):
    def __init__(self, kd):
        print('%s is one kind of the LivingThings' %kd)

    def breath(self):
        print('Living things can breath.')

class Mammal(object):
    def __init__(self, kind):
        print('%s is one kind of the Mammals.' %kind)

    def fur(self):
        print('Mammals have fur.')

class Dog(Mammal, LivingThing):
    pass
d1 = Dog(kind='Dog')  # Dog is one kind of the Mammals.

class Cat(LivingThing, Mammal):
    pass
d1 = Cat(kd='Cat')  # Cat is one of the LivingThings

# 多继承时：
# 如果子类没有构造方法，则先继承哪个类先执行哪个类的构造方法
# 如果子类有构造方法, 但构造方法没有重构父类构造方法,则只执行子类自己的构造方法
# 如果子类有构造方法, 且构造方法重构父类构造方法,则只能执行最先继承的父类的构造方法,且执行最左侧(即最先继承)的父类构造函数



class Bear(LivingThing, Mammal):
    def __init__(self):
        print('Bear\'s init method.')
b1 = Bear()  # Bear's init method.

class Mouse(LivingThing, Mammal):
    def __init__(self):
        super(Mouse, self).__init__(kd='Mouse')  # Mouse is one kind of the LivingThings
m = Mouse()

class Mouse(Mammal, LivingThing):
    def __init__(self):
        super(Mouse, self).__init__(kind='Mouse')  # Mouse is one kind of the Mammals.
m = Mouse()

# class Mouse(Mammal, LivingThing):
#     def __init__(self):
#         super(Mouse, self).__init__(kd='Mouse', kind='Mouse')
# m = Mouse()  # __init__() got an unexpected keyword argument 'kd'


# 经典类与新式类的继承顺序
# class A(object):
class A:
    def __init__(self):
        print('A')
    def foo(self):
        print('A foo')

class B(A):
    # def __init__(self):
    #     print('B')
    pass
    # def foo(self):
    #     print('B foo')

class C(A):
    def __init__(self):
        print('C')
    pass
    # def foo(self):
    #     print('C foo')

class D(B, C):
    # def __init__(self):
    #     print('D')
    pass
    # def foo(self):
    #     print('D foo')

d = D()
d.foo()

# 查找策略：
    # 广度优先：先查找同一层级，同一层级都没有，查找上一层级
    # 深度优先：先直系查找，再旁系查找
# python2 深度优先 经典类方式是按深度优先进行检索，新式类按广度优先
# python3 都是广度优先
