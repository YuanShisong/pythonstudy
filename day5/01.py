'''
模块
    定义：
        本质就是.py结尾的python文件，用来从逻辑上组织python代码


'''

# # import moudle1
# #
# # print(moudle1.name)
# #
# # moudle1.sayhi()
#
# # from module import * 导入模块中所有代码
# # import module 导入整个模块 两者是有区别的
# from moudle1 import *
# def sayhi():
#     print('main')
#
# print(name)  # joshua
#
# sayhi()  # main
#
# from moudle1 import sayhi as mhi
#
# mhi()

# 导入多个
# import module1, module2, module3

# 2、导入其他目录下的模块
# sys.path模块

# 3、导入包 导入包的本质就是执行包下的__init__.py文件

import testdir
testdir.modeltest.model()  # model method

