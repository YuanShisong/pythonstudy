
'''
局部变量
    局部变量和全局变量同名时,局部变量的定义要在引用之前
    global关键字
'''

# 1、局部变量和全局变量同名时,局部变量的定义要在引用之前
var = 1
def func():
    # -------这样会报错-------
    # print(var)
    # var = 2
    # -------这样会报错-------

    # -------如果局部变量和全局变量同名,在使用局部变量前需要先定义--------
    var = 2
    print(var)

print(var)


# 2、global关键字
print('------------test2-------------')
var = 1
def func():
    # ------不能将变量声明为global后在同一行赋值------
    # global var = 3
    # ------不能将变量声明为global后在同一行赋值------
    global var
    print(var)  # 1
    var = 2
    print(var)  # 2
func()
print(var)  # 2
''' 结果>>:
------------test2-------------
1
2
2
'''


# print('------------test3-------------')
# def func():
#     global name
#     name = 'joshua'
# print(name)  # NameError: name 'name' is not defined

print('------------test4-------------')
names = ['a', 'b', 'c']
# names = ('a', 'b')
def func():
    names[0] = 'd'
    print(names)
func()
print(names)
'''结果>>:
------------test4-------------
['d', 'b', 'c']
['d', 'b', 'c']
'''