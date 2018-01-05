
# 字典
'''
特性：
    1、无序

'''

stu = {
    'six':'kongming',
    '07seven':'huangzhong',
    'stu01':'zhangfei',
    'stu03':'liubei',
    'stu04':'guanyu',
    'five':'zhaoyun',
}
# stu['08']= 'machao'
print(stu)
stu.popitem()
print(stu)
c = stu.copy()
print(c)
print(stu['six'])
stu.clear()
print(stu)
c = stu.fromkeys("a")
print(c)






