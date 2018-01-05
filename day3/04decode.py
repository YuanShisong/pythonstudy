# -*- coding:utf-8 -*-
# utd8 --> gbk
import sys
'''
s = u"你好"

utf8code = s.encode('utf-8')
print(utf8code.decode('utf-8'))
print(utf8code, type(utf8code))  # b'\xe4\xbd\xa0\xe5\xa5\xbd' <class 'bytes'>

print(utf8code.decode('gbk'))
'''

s = '你好'
print(type(s))
utf8code = s.encode('utf-8')
print(utf8code)
gbkcode = utf8code.decode().encode("gbk")
print(gbkcode)
print(gbkcode.decode('gbk'))