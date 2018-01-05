'''
面向过程编程
面向对象编程
函数式编程

python 中函数可以返回多个值, 返回的值组织成一个元组
返回值个数，和返回值类型关系
    0个：返回None
    1个：返回object
    多个：返回元组

带参函数
    参数个数必须和函数定义中对应
    调用函数时可以变换位置,但要指定参数名
def test1(x, y):
    print(x, y)
test1(y=1, x=2)  # 可以变换位置,但要指定参数名
'''
# 定义函数

def func1():
    "function1"
    print("function1")
    return 1;

def func2():
    "function1"
    print("function2")

x = func1()
y = func2()
print(x)
print(y)

def test1():
    return
def test2():
    return 0
def test3():
    return 1, '123', ('1','2','4'), {'key':'value'}
def test4():
    # return test3  # <function test3 at 0x0000000002449158>
    return test3()  # (1, '123', ('1', '2', '4'), {'key': 'value'})

x =test1()
y =test2()
z =test3()

print(x)
print(y)
print(z)
for i in z:
    print(i)
print(test4())

'''
有参函数
    位置参数：调用时传入值和函数声明一一对应
    关键字参数：调用时指定关键字
    默认参数：定义函数时指定参数默认值,调用时可以不指定默认参数的值
    参数组：相当于Java中可变参数, 通过*定义, 函数内部将参数处理为元组
        key-value参数：通过**定义，调用时以关键字参数形式调用,把N个关键字参数转换成字典的形式
        *args:接收N个位置参数, 转换成元组的形式
        **kwargs:接收N个关键字参数，转换成字典的形式
    参数组必须放到最后边,和Java一样
'''
print('----------------------')
def test1(x, y):
    print(x, y)
# 1、位置参数
# test1(1)  # TypeError: test1() missing 1 required positional argument: 'y'
# test1(1,2)
# test1(1,2,3)  # TypeError: test1() takes 2 positional arguments but 3 were given

# 2、关键字参数
test1(y=1, x=2)  # 2 1 可以变换位置,但要指定参数名

x = 1
y = 2
test1(x = x, y = y)  # 1 2

# test1(x = 1, 2)  # SyntaxError: positional argument follows keyword argument
test1(1, y=2)  # 1 2 但这样是可以的, 真逗
# test1(1, x=2)  # 不可以,但也不报错,无结果
# test1(x = 1)  # 无结果

# 3、默认参数
def test2(x, y = 2):
    print("test2:", x, y)
test2(1)
test2(1,4)

# 4、参数组
def test3(*args):
    print(args)
test3(1,2,3,3,4,5,56,7,78,8,9)  # (1, 2, 3, 3, 4, 5, 56, 7, 78, 8, 9)

# 5、key-value参数
def test4(**kwargs):
    ":keyword"
    print(kwargs)
test4(name='joshua', age=29, sex='Male')  # {'name': 'joshua', 'age': 29, 'sex': 'Male'}s
test4(**{'name':'joshua', 'age':29})  # {'name': 'joshua', 'age': 29}
# test4({'name':'joshua', 'age':29})  # 这样不行, 为什么呢???
