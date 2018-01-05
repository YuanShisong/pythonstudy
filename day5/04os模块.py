# os模块
# >>> import os
# >>> os.getcwd()
# 'D:\\999-Personal\\Python'
# >>>

# 切换目录
# >>> os.chdir('C:\\BJCAAPP')
# >>> os.getcwd()
# 'C:\\BJCAAPP'
# >>>

# 显示当前目录 父目录
# >>> os.curdir
# '.'
# >>> os.pardir
# '..'
# >>>

# 递归创建目录
# >>> os.makedirs('C:\\BJCAAPP\\a\\b\\c')
# >>>
# 递归删除目录
# >>> os.removedirs('C:\\BJCAAPP\\a\\b\\c')
# >>>
# >>> help(os.removedirs)
# Help on function removedirs in module os:
#
# removedirs(name)
#     removedirs(name)
#
#     Super-rmdir; remove a leaf directory and all empty intermediate
#     ones.  Works like rmdir except that, if the leaf directory is
#     successfully removed, directories corresponding to rightmost path
#     segments will be pruned away until either the whole path is
#     consumed or an error occurs.  Errors during this latter phase are
#     ignored -- they generally mean that a directory was not empty.

# mkdir 逐层创建
# >>> os.mkdir('C:\a\b')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# OSError: [WinError 123] 文件名、目录名或卷标语法不正确。: 'C:\x07\x08'
# >>> os.mkdir(r'C:\a\b')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'C:\\a\\b'
# >>> os.mkdir(r'C:\a')
# >>> os.mkdir(r'C:\a\b')
# >>>

# rmdir 逐层删除
# >>> os.rmdir(r'C:\a\b')
# >>>

# 展示目录
# >>> os.listdir('.')
# ['install']
# >>> os.listdir(r'c:\a')
# ['b']
# >>>

# 删除文件
# >>>os.remove()

# 当前系统分隔符
# >>> os.sep
# '\\'
# >>>
# Linux下
# root@localhost:[/root]python
# Python 2.6.6 (r266:84292, Jul 23 2015, 15:22:56)
# [GCC 4.4.7 20120313 (Red Hat 4.4.7-11)] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import os
# >>> os.sep
# '/'
# >>>

# 当前系统换行符
# Windows
# >>> os.linesep
# '\r\n'
# >>>

# Linux
# >>> os.linesep
# '\n'
# >>>

# 环境变量分隔符
# Windows
# >>> os.pathsep
# ';'
# >>>

# Linux
# >>> os.pathsep
# ':'
# >>>

# 系统名称
# >>> os.name
# 'nt'
# >>>

# 执行系统命令
# >>> os.system('dir')
#  驱动器 C 中的卷是 C
#  卷的序列号是 E835-B383
#
#  C:\BJCAAPP 的目录
#
# 2017/11/29  19:25    <DIR>          .
# 2017/11/29  19:25    <DIR>          ..
# 2017/11/08  10:09    <DIR>          install
#                0 个文件              0 字节
#                3 个目录 38,625,972,224 可用字节
# 0
# >>>

# 目录和文件名分割 其实就是截取最后一个路径分隔符
# >>> os.path.split(r'a\v\d.txt')
# ('a\\v', 'd.txt')
# >>>

# 取目录名和 取文件名
# >>> os.path.dirname(r'a\v\d.txt')
# 'a\\v'
# >>> os.path.basename(r'a\v\d.txt')
# 'd.txt'
# >>>


# 判断输入路径是否存在
# >>> os.path.exists(r'a\v\d.txt')
# False
# >>> os.path.exists(r'C:\a')
# True
# >>>

# 判断是否绝对路径
# >>> os.path.isabs(r'c:')
# False
# >>> os.path.isabs(r'c:\a')
# True
# >>>
# Linux的判断机制很简单，只是看开始字符是否'/'字符，一下代码为Windows平台下运行
# >>> os.path.isabs(r'/a/b/c')
# True
# >>> os.path.isabs(r'a/b/c')
# False
# >>>

# 判断是否文件或路径 如果文件或路径不存在则返回False
# >>> os.path.isfile(r'c:\a\1.txt')
# False
# >>> os.path.isfile(r'c:\a\1.txt')
# True
# >>>
# >>> os.path.isdir(r'c:\a\b')
# True
# >>> os.path.isdir(r'c:\a\c')
# False
# >>>

# 将多个路径拼接 最后一个绝对路径之前的路径将被忽略
# Windows
# >>> os.path.join('c:\\a\\b', 'c\\', '1.txt')
# 'c:\\a\\b\\c\\1.txt'
# >>>
# >>> os.path.join('c:\\a\\b', 'c:\\a\\', '1.txt')
# 'c:\\a\\1.txt'
# >>>


# Linux下
# >>> os.path.join('/home', 'a.file')
# '/home/a.file'
# >>> os.path.join('/home', '/joshua', 'a.file')
# '/joshua/a.file'
# >>> os.path.join('/home', 'joshua', 'a.file')
# '/home/joshua/a.file'
# >>>

# 获取修改最后访问时间和最后修改时间
# >>> os.path.getatime('c:\\a\\1.txt')
# 1511956065.553473
# >>> os.path.getmtime('c:\\a\\1.txt')
# 1511956065.553473
# >>>
