
# 继承 Python可多继承

# class People:  # 经典类
class People(object):  # 新式类 新式类顶级父类是object
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 只能有一个构造函数,如果写多个：后一个会覆盖前一个
    # def __init__(self, name, age, weight):
    #     self.name = name
    #     self.age = age
    #     self.weight = weight
    def eat(self):
        print("%s is eating" %self.name)

    def sleep(self):
        print("%s is sleeping" %self.name)

    def talk(self):
        print("%s is talking" %self.name)

class Relation(object):

    def __init__(self):
        print("Relation name: %s" %self.name)

    def make_friends(self, obj):
        print("%s is making friend with %s" %(self.name, obj.name))

# 子类1
class Man(People):

    # 子类重构 构造函数
    def __init__(self, name, age, money):
        People.__init__(self, name, age)
        # super(Man, self).__init__(name, age)  # 和上一种方式等价  # 新式类
        self.money = money
        print("%s has %s money." %(name, money))

    def marathon(self):
        print("%s is running" %self.name)
    # 重构父类方法
    def sleep(self):
        People.sleep(self)  # 注意传参数
        print("And he is snoring")

josh = Man("Joshua", 29, 10000000)
josh.eat()
josh.sleep()
josh.marathon()

# 子类2 多继承时：如果子类没有构造方法，则先继承哪个类先执行哪个类的构造方法
class Woman(People, Relation):
# class Woman(Relation, People):
    def birth(self):
        print("%s is in labor." %self.name)
mon = Woman('Monica', 25)
mon.birth()

mon.make_friends(josh)  # Monica is making friend with Joshua