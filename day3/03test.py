'''
需求：
    实现一个简单的shell sed功能, 即替换
思路:
    需要输入三个参数:
        1、要替换的文件
        2、被替换的字符
        3、替换字符
    获取参数
        如果文件能找到,进行替换操作
        不能找到, 给提示
    替换操作,
        读取文件, 创建新文件, 逐行读取文件 并判断,如果包含指定字符 直接替换, 逐行写入到新文件
'''

import sys

args = sys.argv
# print(args.count(0))
# if args.count(0) < 2:
#     print("请输入合法参数")
# else :
if True:
    rd = open(args[1], encoding='utf-8')
    wt = open(str(args[1])+'.new', 'w', encoding='utf-8')
    for line in rd:
        if args[2] in rd:
            line = line.replace(args[2], args[3])
        wt.write(line)
rd.close()
wt.close()

