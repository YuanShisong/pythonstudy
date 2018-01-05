
'''
递归
    1、递归层级过多会报错,RecursionError: maximum recursion depth exceeded while calling a Python object
    2、python中默认递归层级限制最多999层
        对比Java：没有层级限制,会不听压栈直到栈溢出：Exception in thread "main" java.lang.StackOverflowError
    3、通过sys.setrecursionlimit()设置允许的最高递归层级
        最大能设置C语言中long类型允许值
        不能设置太小最小为4
        # sys.setrecursionlimit(99999999999999999)  # OverflowError: Python int too large to convert to C long
        # sys.setrecursionlimit(1)  # RecursionError: cannot set the recursion limit to 1 at the recursion depth 1: the limit is too low
'''


# 1、python中递归有层级限制RecursionError: maximum recursion depth exceeded while calling a Python object
def func():
    print('func')
    func()  # RecursionError: maximum recursion depth exceeded while calling a Python object
# func()

# 2、共可以递归999层
def func(n):
    n += 1
    print(n)
    func(n)
# func(1)
'''结果>>:
1
2
3
...
999
'''

# 3、设置递归层级
import sys
# sys.setrecursionlimit(99999999999999999)  # OverflowError: Python int too large to convert to C long
# sys.setrecursionlimit(1)  # RecursionError: cannot set the recursion limit to 1 at the recursion depth 1: the limit is too low
print(1<<20)
sys.setrecursionlimit(4)
func(1)
'''结果>>:(在我本机上)
1
2
3
.....
3222
进程已结束,退出代码-1073741571 (0xC00000FD)
'''

