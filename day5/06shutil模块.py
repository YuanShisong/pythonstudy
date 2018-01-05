
# shutil模块
import shutil

# # copyfileobj 通过流copy
# src = open('MakeMoreTime.txt')
# des = open('MakeMoreTime2.txt', 'w')
# shutil.copyfileobj(src, des)
# src.close()
# des.close()
#
# # copyfile 通过文件名直接copy
# shutil.copyfile('MakeMoreTime.txt', 'MakeMoreTime3.txt')

# 仅copy权限
# shutil.copymode(src, dst)
# Linux上试一下

# copystat 只拷贝文件信息包括获取时间,修改时间等。 如果目标文件不存在则报错
# shutil.copystat('MakeMoreTime.txt', 'MakeMoreTime3.txt')
# shutil.copystat('MakeMoreTime.txt', 'abc.txt')  # FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'abc.txt'

# copy 文件和权限都copy

# copy2 文件和信息都copy

# copytree 递归copy
# shutil.copytree('testdir', 'newdir')

# 递归删除 rmtree
# shutil.rmtree('newdir')

# 递归的移动文件
# shutil.move()

# 打包
# shutil.make_archive()
# shutil.make_archive('testarchive', 'zip', 'testdir')

# make_archive()底层通过zipfile 和tarfile 实现
import zipfile
z = zipfile.ZipFile('testzipfile.zip', 'w')
z.writestr('a.txt', 'this is a test program')
z.writestr('a.txt', 'ZIPFILE')
z.writestr('a.txt', 'it is ')
z.writestr('a.txt', 'about to end ')
z.writestr('a.txt', 'make more time')
z.close()

