
'''
高阶函数：
    将函数作为参数传递给另一个函数
    注意和函数调用后的返回值传递给另一个函数的区别
'''

def absAdd(a, b, f=abs):
    return f(a) + f(b)
rtn = absAdd(4,-8)
print(rtn)
'''结果>>:
12
'''

def myf(n):
    return n / 2
rtn = absAdd(4,-8, myf)
print(rtn)
'''结果>>:
-2.0
'''
