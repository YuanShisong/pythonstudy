
class Dog:
    fur = "Long"  # 类变量
    attr = []  # 列表类型变量
    # 构造函数
    def __init__(self, name, age = 20, sex = 'male', fur = "Long"):
        self.name = name  # 实例变量
        self.__age = age  # "__"定义私有属性
        self.sex = sex
        fur = fur
    def bark(self):  # 类的方法
        print(self.name, 'wang wang wang')

    # 析构函数
    def __del__(self):
        print(self.name, ': Oh I die')

    # 访问私有属性 getter
    def getAge(self):
        print("%s is %s years old." %(self.name, self.__age))

    # 设置私有属性 setter
    def setAge(self, age = 20):
        self.__age = age
        print("%s's age has changed it's %s years old now." %(self.name, self.__age))

    # 私有方法 同样通过"__"定义
    def __test(self):
        print("Method __test")

    def test(self):
        self.__test()

d1 = Dog('Shapi', 30, 'female')
d2 = Dog('Bianmu')

d1.bark()
# 添加属性
d1.smart = True
print(d1.smart)
# 删除属性
# del d1.name
# print(d1.name)  # 'Dog' object has no attribute 'name'

# 通过实例修改类变量：可以修改
d1.fur = 'short'
d1.attr.append("small")
d2.attr.append("smart")
print(d1.fur)  # short
del d1  # Shapi : Oh I die
print(d2.fur)  # Long
print(d2.attr)  # ['small', 'smart'] 浅copy

# print(d2.__age)  # 'Dog' object has no attribute '__age'
d2.getAge()
d2.setAge(5)

# d2.__test()
d2.test()

# d2.bark()
# print(d1.fur)
# print(d1.name)

# print(c1)

# 析构函数
# 在实例释放和销毁的时候执行，通常用于做一些收尾工作，如关闭数据库链接，关闭文件

d3 = Dog('Labuladuo', 6, 'male')