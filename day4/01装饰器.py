
'''
装饰器
    定义：本质是函数，装饰其他函数（就是为其他函数添加附加功能）
    原则：
        1、不能修改被装饰函数的源代码
        2、不能修改被装饰的函数的调用方式****
        也就是对于被装饰函数来说装饰器是透明的

'''

import time

# 0、统计程序运行时间的装饰器
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func()#         end = time.time()
#         print('The function takes %s seconds.' % (end - start))
#         # print('The function:%s takes seconds.' % func.__name__)
#     return wrapper  #
#
# @timer
# def test1():
#     time.sleep(3)
#     print('test1 ends.')
#
# test1()
#
# print(timer)

# 1、能修改被装饰函数的源代码,给方法添加功能
#   给方法a，添加统计运行时间的功能
# print('--------step1-------------')
# import time
# def a():
#     time.sleep(1)
#     print('a')
# def timer(func):
#     start = time.time()
#     func()
#     end = time.time()
#     print('It takes %s seconds.' % (end - start))
# timer(a)
'''结果>>:（修改了调用方式）
a
It takes 1.0000569820404053 seconds.
'''

# # 2、不修改被装饰的函数的调用方式，在目标方法前添加功能，此时不需要高阶函数即可实现
# print('-------step2----------------')
# def a():
#     time.sleep(1)
#     print('a')
#
# def test(func):
#     print('test')
#     return func
# a = test(a)
# a()

# # 3、不用内嵌函数能实现吗
# print('----------只能在目标代码前添加代码---------')
# def timer(func):
#     print('before func')
#     return func
#
# def a():
#     print('a')
#
# a = timer(a)
# a()
# # 貌似不可以


# 装饰器：不改变目标代码，不改变目标代码调用方式
# 通过高阶函数实现装饰, 在目标代码前后都能加上功能
# def timer(func):
#     def wrapper():
#         print('before func')
#         func()
#         print('after func')
#     return wrapper
#
# def a():
#     print('a')
#
# @timer
# def b():
#     print('a')
# b()
# a = timer(a)
# a()

# 4、带参数的装饰器
# def timer(func):
#     def wrapper(*args,**kwargs):
#         print('before func')
#         func(*args,**kwargs)
#         print('after func')
#         print('--------------------')
#     return wrapper
#
# # 无参数
# def a():
#     print('a')
#
# # 一个参数
# def b(arg):
#     print('b and args are:', arg)
#
# # 多个参数
# def c(arg1, arg2, arg3, arg4):
#     print('c and args are:', arg1, arg2, arg3, arg4)
#
# a = timer(a)
# a()
#
# b = timer(b)
# b('bbb')
#
# c = timer(c)
# c("123", "3434", ['2','4','4'],('1','3',3))

'''结果>>:
before func
a
after func
--------------------
before func
b and args are: bbb
after func
--------------------
before func
c and args are: 123 3434 ['2', '4', '4'] ('1', '3', 3)
after func
--------------------
'''


# 5、带参数带返回值的装饰器 装饰带返回值的函数
'''
需求：
    模拟四个登录页面, index home bbs page1
        index 不需要认证可以直接登录
        home 需要认证,认证方式为本地认证
        bbs 也需要认证,但认证方式为ldap
        page1 页面也需要认证,但认证方式不支持
    通过同一个装饰器实现以上功能
'''
# user = 'joshua'
# pswd = '123'
#
# # def auth(*args, **kwargs):  # *args, **kwargs是装饰器的后括号中的参数，如@auth('ldap') 此处参数肯定不能是可变参数,而应该是定义装饰器是就已定义的参数，最好用关键字参数
# def auth(authWay):  # *args, **kwargs是装饰器的后括号中的参数，如@auth('ldap')
#     def outer(func):  # func参数是被装饰方法
#         def wrapper(*args, **kwargs):
#             if 'file' == authWay:
#                 username = input('Username:').strip()
#                 password = input('Password:').strip()
#                 if username == user and pswd == password:
#                     print('\033[32;1mFILE Authenticated.\033[0m')
#                     return func(*args, **kwargs)  # 如果有返回值,将func()的执行结果返回即可
#                 else:
#                     exit('\033[33;1mFILE Authenticated FAILURE Invalid username or password.\033[0m')
#             elif 'ldap' == authWay:
#                 return func(*args, **kwargs)
#                 print('\033[32;1mLDAP Authenticated.\033[0m')
#             else:
#                 exit('\033[33;1mCannot Authenticate this way.\033[0m')
#         return wrapper
#     return outer
#
# def index():
#     print('index')
#
# @auth(authWay='file')
# def home():
#     print('home')
#     return 'Welcome to home.'
#
# @auth(authWay='ldap')
# def bbs():
#     print('bbs')
#     return 'Welcome to bbs.'
#
# @auth(authWay='abc')
# def page1():
#     print('page1')
#     return 'Welcome to page1.'
#
# index()
#
# print('---------------\n')
# print(home())
#
# print('---------------\n')
# print(bbs())
#
# print('---------------\n')
# print(page1())


def a(arg):
    print('a', arg)
    return 'return value:a'

def b(fun):
    def c(*args, **kwargs):
        print('before')
        return fun(*args, **kwargs)
        print('after')
    return c

a = b(a)

print(a('1'))
