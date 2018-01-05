
#
# class Foo(object):
#     # __metaclass__ = MyType
#     def __init__(self, name):
#         self.name = name
#         print("Foo __init__")
#
#     def __new__(cls, *args, **kwargs):
#         '''
#         实例化时会执行__new__而且先于__init__执行
#         __new__触发__init__方法
#         :param args:
#         :param kwargs:
#         :return:
#         '''
#         print("Foo __new__", ', ', cls, ', ', *args, ', ', **kwargs)
#         return object.__new__(cls)
#         # object.__new__(cls)  # f: None
#         # return super.__new__(cls)  # TypeError: super.__new__(Foo): Foo is not a subtype of super
#
# f = Foo("Joshua")
# '''
# Foo __new__ <class '__main__.Foo'> Joshua
# Foo __init__
# '''
# print("f:", f)
# print("fname", f.name)


# class MyType(type):
#     def __init__(self, *args, **kwargs):
#         print("Mytype __init__", *args, **kwargs)
#
#     def __call__(self, *args, **kwargs):
#         print("Mytype __call__", *args, **kwargs)
#         obj = self.__new__(self)
#         print("obj ", obj, *args, **kwargs)
#         print(self)
#         self.__init__(obj, *args, **kwargs)
#         return obj
#
#     def __new__(cls, *args, **kwargs):
#         print("Mytype __new__", *args, **kwargs)
#         return type.__new__(cls, *args, **kwargs)
#
#
# print('here...')
#
#
# class Foo(object, metaclass=MyType):
# # class Foo(object):
#     __metaclass__ = MyType
#     def __init__(self, name):
#         self.name = name
#         print("Foo __init__")
#
#     def __new__(cls, *args, **kwargs):
#         print("Foo __new__", cls, *args, **kwargs)
#         return object.__new__(cls)
#
#
# f = Foo("Joshua")
# print("f", f)
# print("fname", f.name)

# '''
# python2中可以以此方式__metaclass__ = MyType
#     指定metaclass
#     here...
#     Mytype __new__
#     Mytype __init__
#     Mytype __call__
#     Foo __new__
#     ('obj ', <__main__.Foo object at 0x2ab85af975d0>)
#     <class '__main__.Foo'>
#     Foo __init__
#
# python3中需要以这种方式指定metaclass
#     class Foo(object, metaclass=MyType):
#     ,否则输出结果如下
#     here...
#     Foo __new__ <class '__main__.Foo'> Joshua
#     Foo __init__
#     f <__main__.Foo object at 0x0000000002218908>
#     fname Joshua
# '''


# class MyType(type):
#     def __init__(self, *args, **kwargs):
#         print("Mytype __init__", *args, **kwargs)
#
#     def __call__(self, *args, **kwargs):
#         print("Mytype __call__", *args, **kwargs)
#         obj = self.__new__(self)  # 调用Foo的__new__方法
#         print("obj ",obj,*args, **kwargs)
#         print(self)
#         self.__init__(obj,*args, **kwargs)  # 调用Foo的__init__方法
#         return self
#
#     def __new__(cls, *args, **kwargs):
#         print("Mytype __new__", *args, **kwargs)
#         return type.__new__(cls, *args, **kwargs)
# print('here...')
#
# class Foo(object, metaclass=MyType):
#     def __init__(self, name):
#         self.name = name
#         print("Foo __init__")
#
#     def __new__(cls, *args, **kwargs):
#         print("Foo __new__", cls, *args, **kwargs)
#         return object.__new__(cls)
# '''
#     1、Foo类是MyType的实例化(metaclass=MyType),执行到class Foo(object,metaclass=MyType):时要调用__new__和__init__方法来实例化一个MyType对象,即Foo类
# '''
# f = Foo("Joshua")
# '''
#     2、执行Foo('Joshua')(对对象加()调用),即对Foo类进行实例化,需要执行Foo对象对应类的内置方法__call__
#     3、
# '''
#
# # print("f", f)
# # print("fname", f.name)

# https://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
'''
类就是对象
    1、借鉴于Smalltalk语言。borrowed from the Smalltalk language.
    2、大多数语言中类是用来定义如何创建对象的代码段, Python中类也有同样作用，但不止于此：类也是对象
        >>> class ObjectCreator(object):
        ...       pass
        ... 
        在python中只要用了class关键字,python就执行它(class)在内存中创建对象,以上代码结束后,python在内存中创建了一个名为ObjectCreator的对象
        这个对象和普通对象有所不同：这个对象本身能创建其他对象(实例),所以这个对象也是一个类
        但这个对象依然是对象，因此你能：
            1)将他赋值给一个变量
            2)拷贝他
            3)给他设置属性
            4)将他当做方法的参数传递

            >>> print(ObjectCreator) # 打印此对象
            <class '__main__.ObjectCreator'>
            >>> def echo(o):
            ...       print(o)
            ... 
            >>> echo(ObjectCreator) # 将此对象当做方法的参数
            <class '__main__.ObjectCreator'>
            >>> print(hasattr(ObjectCreator, 'new_attribute'))
            False
            >>> ObjectCreator.new_attribute = 'foo' # 给此对象添加属性
            >>> print(hasattr(ObjectCreator, 'new_attribute'))
            True
            >>> print(ObjectCreator.new_attribute)
            foo
            >>> ObjectCreatorMirror = ObjectCreator # 将此对象赋值给一个变量
            >>> print(ObjectCreatorMirror.new_attribute)
            foo
            >>> print(ObjectCreatorMirror())
            <__main__.ObjectCreator object at 0x8997b4c>
动态生成类
    因为类就是对象,因此能像其他对象一样在运行中生成类。
    首先你可以在方法中用class关键字创建一个class
        >>> def choose_class(name):
        ...     if name == 'foo':
        ...         class Foo(object):
        ...             pass
        ...         return Foo # 返回Foo类,而不是对象
        ...     else:
        ...         class Bar(object):
        ...             pass
        ...         return Bar
        ...
        >>> MyClass = choose_class('foo')
        >>> print(MyClass) # 方法返回类,不返回对象
        <class '__main__.Foo'>
        >>> print(MyClass()) # 可以通过方法返回的类创建对象
        <__main__.Foo object at 0x89c6d4c>
    但这并不是动态创建的，因为你仍然需要自己写出整个class
    既然类是对象，那么类对象必须是由其他什么东西生成。当你用class关键字时，Python自动为你创建类对象，但就像Python中其他大部分things一样，Python提供了手动创建类对象的方式。
    那就是type,它能告诉你一个对象的类型，如下代码
        >>> print(type(1))
        <type 'int'>
        >>> print(type("1"))
        <type 'str'>
        >>> print(type(ObjectCreator))
        <type 'type'>
        >>> print(type(ObjectCreator()))
        <class '__main__.ObjectCreator'>
    type还有一个完全不同的功能，它还能运行中创建类对象，type方法能将"类的描述信息"做为参数，并返回类对象
    (我知道同一个方法针对不同的参数提供不同功能这种方式很笨)
    type这样使用
        type(类对象的名称, 元组形式的所有父类对象 (继承用，可以为空),包含属性名和属性值的字典)
    例如
        >>> class MyShinyClass(object):
        ...       pass
    可以如下描述
        >>> MyShinyClass = type('MyShinyClass', (), {}) # 返回一个类对象
        >>> print(MyShinyClass)
        <class '__main__.MyShinyClass'>
        >>> print(MyShinyClass()) # 通过返回的类对象创建一个对象
        <__main__.MyShinyClass object at 0x8997cec>
    你应该注意到，我用“MyShinyClass”做接收类对象的变量名和类对象的名称，这两者是可以不同的。
    type接收一个字典来定义类的属性，如下
        >>> class Foo(object):
        ...       bar = True
    可以这样描述
        >>> Foo = type('Foo', (), {'bar':True})
    它能像正常类一样使用
        >>> print(Foo)
        <class '__main__.Foo'>
        >>> print(Foo.bar)
        True
        >>> f = Foo()
        >>> print(f)
        <__main__.Foo object at 0x8a9b84c>
        >>> print(f.bar)
        True
    当然你也能将其当做基类，如下：
        >>>   class FooChild(Foo):
        ...         pass
    可以这样描述：
        >>> FooChild = type('FooChild', (Foo,), {})
        >>> print(FooChild)
        <class '__main__.FooChild'>
        >>> print(FooChild.bar) # bar is inherited from Foo
        True
    如果你想要给类添加方法，只要定义一个合适的方法并将其指定给类对象的一个属性即可，如下
        >>> def echo_bar(self):
        ...       print(self.bar)
        ...
        >>> FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
        >>> hasattr(Foo, 'echo_bar')
        False
        >>> hasattr(FooChild, 'echo_bar')
        True
        >>> my_foo = FooChild()
        >>> my_foo.echo_bar()
        True
    你甚至可以在类对象被动态创建后各类添加方法，就像给其他普通(通过class关键字创建的)类对象添加方法一样：
        >>> def echo_bar_more(self):
        ...       print('yet another method')
        ...
        >>> FooChild.echo_bar_more = echo_bar_more
        >>> hasattr(FooChild, 'echo_bar_more')
        True
    现在你知道我要表达什么了吧：在Python里，类就是对象，你能在运行中动态的创建类。
    这就是你用class关键字时Python做的事情，metaclass也是这样
那到底什么是metaclass呢(终于！！！)
    Metaclasses是创建class的"东西"
    你定义类是为了创建对象对吧? 但是我们已经知道,Python里类就是对象。Metaclass呢，就是创建这种对象(类)的东西.他们是描述类的类，你可以将Metaclass想象成以下形式：
        MyClass = MetaClass()
        MyObject = MyClass()
    你已经知道，type能让你做如下事情:
        MyClass = type('MyClass', (), {})
    这是因为方法type实际上是一个Metaclass,type是Python用来创建其他类的Metaclass。
    你可以通过__class__属性来验证这一点
    也就是说type就是用来创建其他class的class
    在Python中一切皆对象，一切皆对象，包括int str function(方法) class(类)，所有一切都是对象，而且他们都是有某一个类创建
        >>> age = 35
        >>> age.__class__
        <type 'int'>
        >>> name = 'bob'
        >>> name.__class__
        <type 'str'>
        >>> def foo(): pass
        >>> foo.__class__
        <type 'function'>
        >>> class Bar(object): pass
        >>> b = Bar()
        >>> b.__class__
        <class '__main__.Bar'>
    那么所有__class__的__class__是什么呢？
        >>> age.__class__.__class__
        <type 'type'>
        >>> name.__class__.__class__
        <type 'type'>
        >>> foo.__class__.__class__
        <type 'type'>
        >>> b.__class__.__class__
        <type 'type'>
    所以一个metaclass就是用来创建类对象的东西，你可以称之为“类工厂”。而type就是Python內建的metaclass(类工厂)，当然你能定义你自己的metaclass
    
__metaclass__属性
    当你创建类时，可以给其添加__metaclass__属性
        python2.x的写法
        class Foo(object):
            __metaclass__ = something...
            [...]
        python3.x的写法
        class Foo(object, metaclass=something...):
            [...] 
    这样做Python会通过你指定的metaclass创建Foo类
    下边这点稍难理解，请注意
    在class Foo(object)，这时内存中还没有创建Foo类对象。Python会先在类定义代码中找__metaclass__属性，找到的话就用你指定的metaclass创建Foo类对象，找不到就通过type创建Foo类对象。
    当执行下边代码时：
        class Foo(Bar):
            pass
    Python会：
        1、在Foo中有没有指定__metaclass__属性
        2、如果找到，就会通过__metaclass__指定的东西创建Foo类对象(注意此处是类对象)
        3、如果找不到，就会去MODULE(模块)级别去找，并创建Foo类对象(但只适用于没有继承任何父类的类,基本上就是老式类)
        4、如果都找不到，就会通过Bar(第一个父类)的metaclass(很有可能是type)来创建Foo类对象,
        5、这里要注意__metaclass__不会被继承，而父类的__class__(Bar.__class__)会被子类继承.即：如果Bar用了__metaclass__属性通过type()而不是type.__new__()创建Bar类对象,那么子类不会继承这种行为。
    现在问题是：可以将什么指定给__metaclass__。
    答案是：能创建类的东西。
    什么能创建类呢？type type的子类 和所有使用type的

自定义metaclass
    metaclass的主要作用就是创建类时使类发生变化
    通常做API时才会用到，就是创建和上下文相吻合的类(这句翻的太烂)。
    举个例子：你决定所有模块下的类的属性都要大写，有很多种方法实现此需求，其中一种就是在module级别设置__metaclass__属性。
    这样一来，此模块下所有类都通过指定的metaclass创建，你只需要告诉metaclass将所有属性大写即可。
    幸运的是__metaclass__只要可被调用即可，它不必是一个类。
    所以我们先举个例子，用一个方法做metaclass
        # the metaclass will automatically get passed the same argument that you usually pass to `type`
        def upper_attr(future_class_name, future_class_parents, future_class_attr):
          """
            Return a class object, with the list of its attribute turned
            into uppercase.
          """

          # pick up any attribute that doesn't start with '__' and uppercase it
          uppercase_attr = {}
          for name, val in future_class_attr.items():
              if not name.startswith('__'):
                  uppercase_attr[name.upper()] = val
              else:
                  uppercase_attr[name] = val

          # let `type` do the class creation
          return type(future_class_name, future_class_parents, uppercase_attr)

        __metaclass__ = upper_attr # this will affect all classes in the module

        class Foo(): # global __metaclass__ won't work with "object" though
          # but we can define __metaclass__ here instead to affect only this class
          # and this will work with "object" children
          bar = 'bip'

        print(hasattr(Foo, 'bar'))
        # Out: False
        print(hasattr(Foo, 'BAR'))
        # Out: True

        f = Foo()
        print(f.BAR)
        # Out: 'bip'
    现在，我们用一个类做metaclass来实现
        # remember that `type` is actually a class like `str` and `int`
        # so you can inherit from it
        class UpperAttrMetaclass(type):
            # __new__ is the method called before __init__
            # it's the method that creates the object and returns it
            # while __init__ just initializes the object passed as parameter
            # you rarely use __new__, except when you want to control how the object
            # is created.
            # here the created object is the class, and we want to customize it
            # so we override __new__
            # you can do some stuff in __init__ too if you wish
            # some advanced use involves overriding __call__ as well, but we won't
            # see this
            def __new__(upperattr_metaclass, future_class_name,
                        future_class_parents, future_class_attr):

                uppercase_attr = {}
                for name, val in future_class_attr.items():
                    if not name.startswith('__'):
                        uppercase_attr[name.upper()] = val
                    else:
                        uppercase_attr[name] = val

                return type(future_class_name, future_class_parents, uppercase_attr)
    上面的方式不是很"面向对象"，因为我们直接调用了type方法，而且没有重写也没有调用父类的__new__方法，下面这种方式就好一些
        class UpperAttrMetaclass(type):
            def __new__(upperattr_metaclass, future_class_name,
                        future_class_parents, future_class_attr):

                uppercase_attr = {}
                for name, val in future_class_attr.items():
                    if not name.startswith('__'):
                        uppercase_attr[name.upper()] = val
                    else:
                        uppercase_attr[name] = val

                # reuse the type.__new__ method
                # this is basic OOP, nothing magic in there
                return type.__new__(upperattr_metaclass, future_class_name,
                                    future_class_parents, uppercase_attr)
    你可能已经注意到了参数"upperattr_metaclass"，这个参数并没有什么特殊的，__new__方法总是以所在类中的类对象作为第一个参数，就像普通方法中的self参数一样，将实例作为第一个参数。
    当然我用的名字都见名知意，但就像self，所有的参数也有简短的名字，所以一个真正的metaclass会像下面这样：
        class UpperAttrMetaclass(type):
            def __new__(cls, clsname, bases, dct):

                uppercase_attr = {}
                for name, val in dct.items():
                    if not name.startswith('__'):
                        uppercase_attr[name.upper()] = val
                    else:
                        uppercase_attr[name] = val

                return type.__new__(cls, clsname, bases, uppercase_attr)
    我们可以通过使用super关键字使类更清晰：
        class UpperAttrMetaclass(type):
            def __new__(cls, clsname, bases, dct):

                uppercase_attr = {}
                for name, val in dct.items():
                    if not name.startswith('__'):
                        uppercase_attr[name.upper()] = val
                    else:
                        uppercase_attr[name] = val

                return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)
    就这样。除此之外真的没有其他关于metaclass的信息了。
    The reason behind the complexity of the code using metaclasses is not because of metaclasses, it's because you usually use metaclasses to do twisted stuff relying on introspection, manipulating inheritance, vars such as __dict__, etc.
    实际上，metaclass在做黑魔法时尤其游泳，也就是做复杂的事情。至于metaclass本身，还是很简单的：
        1、拦截类的生成
        2、修改类
        3、返回修改后的类
为什么用metaclass而不用方法呢？
    既然__metaclass__能接收一切可被调用的东西,为什么要用class呢，class可是比方法复杂的多啊！！！
    主要是以下几个原因：
        1、目的更明确。你看到UpperAttrMetaclass(type),就知道是什么意思
        2、能用"面向对象编程"，metaclass可以继承metaclass可以重写父类方法，甚至可以使用其他metaclass。
        3、某个类如果你指定了metaclass，则它的子类是这个metaclass的实例，但如果指定了metaclass为function则不是(一个类不能是某个方法的实例)。
        4、代码结构会更好。上面使用metaclass的例子已经非常简单了，通过使用metaclass的情况都是比较复杂的。将所有方法组织在一个class中，能使你的代码更易读。
        5、可以在__new__,__init__和__call__中做你想做的事，虽然你能都在__new__写，但有些人还是习惯在__init_中实现。
        6、叫metaclass，该死的，这名字还是有些意义的。
为什么你会用metaclass
    现在的主要问题是，为什么要用这么晦涩难懂又容易出错的metaclass呢
    Well，通常你是不需要用的：
        Metaclass是深层魔法(deeper magic)，99%的用户都不需要关心它。如果你好奇什么时候会用到它：你不需要用它。(真正确定自己需要用到metaclass的人，他们不需要知道用它的原因)
    Python Guru Tim Peters
        metaclass的主要用于创建API，典型的例子就是Django ORM。它允许你这样定义：
            class Person(models.Model):
                name = models.CharField(max_length=30)
                age = models.IntegerField()
        但如果你这样做
            guy = Person(name='bob', age='35')
            print(guy.age)
        代码不返回IntegerField对象，而返回int，甚至是直接在数据库中取出的数据。
        这可能是因为，models.Model定义了__metaclass__，而指向的metaclass将你定义的简单的Person类变为数据库中的一个字段。
        利用metaclass，Django暴露一套API使得复杂的事情看起来很简单，而在幕后做真正的工作。
最后
    首先，类就是能创建实例的对象。实际上，类是metaclass的实例
        >>> class Foo(object): pass
        >>> id(Foo)
        142630324
    在Python中一切都是对象(实例)，他们不是类的实例就是metaclass的实例。
    除了type。type的metaclass是自己，实际上在纯Python中是不能创建type的，而是通过在Python的实现层作弊实现的。
    其次，metaclass是很复杂的。如果你只要对类做一点点调整，就不要使用metaclass，你可以用另外两种技术来实现：
        猴子补丁(monkey patching)
        装饰器
    当你需要对类做调整，99%的情况下你可以通过以上两种方式实现。
    但是98%的情况是：你完全不需要对类做调整

'''

# the metaclass will automatically get passed the same argument
# that you usually pass to `type`
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
    Return a class object, with the list of its attribute turned
    into uppercase.
    """

    # pick up any attribute that doesn't start with '__' and uppercase it
    uppercase_attr = {}
    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val

    # let `type` do the class creation
    return type(future_class_name, future_class_parents, uppercase_attr)
# python2:__metaclass__ = upper_attr
# __metaclass__ = upper_attr # this will affect all classes in the module

# python3: metaclass=upper_attr
class Foo(metaclass=upper_attr):  # global __metaclass__ won't work with "object" though
# class Foo():  # global __metaclass__ won't work with "object" though
    # but we can define __metaclass__ here instead to affect only this class
    # and this will work with "object" children
    bar = 'bip'

print(hasattr(Foo, 'bar'))  # False
print(hasattr(Foo, 'BAR'))  # True