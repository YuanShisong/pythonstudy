# 等待用户输入
# username = input("username:")
# password = input("password:");
# print(username,password)

# 字符串拼接

name = input("name:")
age = input("age:")
gender = input("gender:")

# print('''user:''' + gender + ''', name:''' + name + ''', age:''' + age)

'''
    %s做占位符 字符串后跟%s(zwf1, zwf2, zwf3……)
'''
info = '''
-----------info of %s-------
Name:%s
Age:%s
Gender:%s
''' %(name, name, age, gender)

print(info)

'''
%s 代表string
%d 代表数字
%f float
报错
TypeError: %d format: a number is required, not str
'''

print(type(age))  # 打印类型
age = int(age)  # 需要强转为integer
print(type(age))
info2 = '''
-----------info2 of %s-------
Name:%s
Age:%d
Gender:%s
''' %(name, name, age, gender)
print(info2)

# 格式化拼接
info3 = '''
-----------info3 of {a}-------
Name:{a}
Age:{b}
Gender:{c}
'''.format(a=name, b=age, c=gender)
print(info3)

info4 = '''
-----------info4 of {0}-------
Name:{0}
Age:{1}
Gender:{2}
'''.format(name, age, gender)
print(info4)