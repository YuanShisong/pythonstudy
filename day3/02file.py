
# 打开文件

data = open('01set.py', encoding='utf-8').read()
# print(data)

file = open('01set.py', encoding='utf-8')

# d1 = file.read()
# d2 = file.read()
# print(d1)
# print('---------------------------------------------------')  # 为什么没有在d1和d2之间呢
# print(d2)

# def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
'''
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
'''

# tf1 = open('testfile1', 'r', encoding='utf-8')
# tf1.write("You say one love one life")
# r代表只读模式,不能写
# Traceback (most recent call last):
#   File "D:/999-Personal/Python/study/day3/02file.py", line 29, in <module>
#     tf1 = open('testfile1', 'r', encoding='utf-8')
# FileNotFoundError: [Errno 2] No such file or directory: 'testfile1'

# tf1 = open('testfile1', 'w', encoding='utf-8')
# tf1.write("You say one love one life")
# 文件不存在,不会创建文件
# Traceback (most recent call last):
#   File "D:/999-Personal/Python/study/day3/02file.py", line 29, in <module>
#     tf1 = open('testfile1', 'r', encoding='utf-8')
# FileNotFoundError: [Errno 2] No such file or directory: 'testfile1'

# tf1 = open('testfile1', 'x', encoding='utf-8')
# tf1.write("You say one love one life")
# tf2 = open('testfile2', 'w', encoding='utf-8')
# tf2.write('Is it getting better, or do you feel the same.')
# tf2 = open('testfile2', 'a', encoding='utf-8')
# tf2.write('Will it make it easier on you now, you got someone to blame.')
# tf2 = open('testfile2', 'w', encoding='utf-8')
# tf2.write('I have climbed highest mountain, I have run through the field.')

'''
readline 读一行文件
readlines 将文件按行组织成列表
'''

f = open('01set.py', 'r', encoding='UTF-8')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readlines())  # 将文件按行组织成列表

# 迭代器方式
# for line in f:
#     print(line)

'''seek tell 
tell 当前游标索引值(按字符计算)
seek 到指定字符位置
'''
print(f.tell())
print(f.seek(100))
print(f.readline())
print(f.tell())

print(f.encoding)

print(f.fileno())
f = open('01set.py', 'a', encoding='UTF-8')
f.write("# test fileno() method ")
print(f.fileno())  # 写过之后系统版本会变化

print(f.flush())  # 缓存中内容刷到硬盘上

'''truncate()
并非清空文件
而是清空字符,并以空格填充
'''
f2 = open('testfile2', 'w', encoding='utf-8')
# f2.truncate()
# f2.write('But I still have not found what I am looking for.')
# f2.truncate(10)  # start at 10
# f2.write('But I still have not found what I am looking for.')
# f2.truncate()

f2.write('But I still have not found what I am looking for.')
f2.truncate(0)
f2.write('But I still have not found what I am looking for.')

# 读写模式 r+
f3 = open('testfile1', 'r+', encoding='utf-8')
print(f3.readline())
print(f3.readline())
print(f3.readline())
# f3.write("Four little children ")
# f3.write("Four little children ")
f3.close()

# 二进制方式打开文件, 不能传编码参数
f4 = open('testfile1', 'rb')
print(f4.readline())

'''
以二进制方式写入, 系统默认是gbk, 然后以utf-8字符方式读出会乱码吗 
'''
fb = open('testfile3', 'wb')
fb.write('测试,ceshi,test\nYou say one love one life'.encode(encoding='gbk'))
fb.close()
fb = open('testfile3', 'r', encoding='gbk')
print(fb.read())

'''打开文件 不用手动关闭 with 
和创建临时表语法很像
可以同时打开多个
'''
with open('testfile1', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)

import sys
sys.getdefaultencoding()