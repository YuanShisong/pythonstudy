
# 反射
# 根据用户输入选择执行不同方法


def bark(self):
    print('%s goes wang wang wang' % self.name)


def run(self):
    print('%s runs like a wind' % self.name)


class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('%s is eating ' % self.name)

    def sleep(self):
        print('%s is sleeping...' % self.name)


d = Dog("BianMu")
# 获取方法 添加方法
choice = input(">>:").strip()
if hasattr(d, choice):
    getattr(d, choice)()  # 反射获取方法 比起Java好简单 getattr
else:
    # print(d.name, 'can not', choice)
    if choice == 'bark':
        setattr(d, choice, bark)  # 动态添加方法
        d.bark(d)
    elif choice == 'run':
        setattr(d, choice, run)
        d.run(d)
    else:
        print(d.name, 'can not', choice)

# 设置属性 获取属性
# choice = input('输入属性名>>:')
# value = input('输入属性值>>:')
# setattr(d, choice, value)  # 设置属性
# print(choice, ':', getattr(d, choice))  # 获取属性
# print(d.age)

# 删除属性 类成员方法不是属性不能通过delattr删除
# choice = input(">>:").strip()
# if hasattr(d, choice):
#     print(getattr(d, choice))
#     # delattr(d, choice)  # AttributeError: sleep
#     print(hasattr(d, choice))
