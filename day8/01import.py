
# 动态导入模块

import importlib

modname = 'lib.aa'

# 动态导入包
# lib = __import__(modname)  # 导入lib
# print(lib)  # <module 'lib' (namespace)>
# lib = importlib.import_module(modname)  # 直接导入aa.py
# print(lib)  # <module 'lib.aa' from 'D:\\999-Personal\\Python\\study\\day8\\lib\\aa.py'>
# lib.meth()  # aa method

# #调用包下方法
# lib.aa.meth()  # aa method
# #实例化包下类
# c = lib.aa.C()
# print(c)  # <lib.aa.C object at 0x0000000002230B70>
# #调用方法
# c.func()  # func


# c = getattr(lib.aa, 'C')
# print(c)  # <class 'lib.aa.C'>
# c = c()
# print(c)  # <lib.aa.C object at 0x0000000002228A20>

#
# a = getattr(lib, 'aa')
# print(a)  # <module 'lib.aa' from 'D:\\999-Personal\\Python\\study\\day8\\lib\\aa.py'>
# a.meth()  # aa method
# c = a.C()
# print(c)  # <lib.aa.C object at 0x0000000002240CF8>
# c.func()  # func
