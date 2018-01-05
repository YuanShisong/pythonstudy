
#
import random
# >>> random.random()
# 0.17351255078697314

# >>> random.randint(1,10)
# 4
# >>> random.randint(1,10)
# 9
# >>> random.randint(1,10)
# 10
# >>>

# random.randrange(1,2) 不包含2
# >>> random.randrange(1,2)
# 1
# >>> random.randrange(1,2)
# 1
# >>> random.randrange(1,2)
# 1
# >>>

# >>> random.choice('hello world')
# 'w'
# >>> random.choice('hello world')
# 'o'
# >>>

# 任意取指定数量的值 不重复取(相当于袋子里拿出小球) 指定数量不能大于列表长度
# >>> random.sample('hello world', 4)
# ['l', 'o', 'e', 'h']
# >>>

# >>> random.sample('hello world', 50)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "C:\Users\Administrator\AppData\Local\Programs\Python\Python36\lib\random.py", line 317, in sample
#     raise ValueError("Sample larger than population or is negative")
# ValueError: Sample larger than population or is negative
# >>>

# >>> random.sample(range(13), 13)
# [9, 0, 7, 3, 12, 8, 4, 1, 11, 5, 2, 6, 10]
# >>>

# 指定范围取浮点数
# >>> random.uniform(5,7)
# 6.93421997970465
# >>>

# 将列表打乱：random.shuffle()
# >>> items = [1,2,3,4,5,6,7]
# >>> items
# [1, 2, 3, 4, 5, 6, 7]
# >>> print(random.shuffle(items))
# None
# >>> random.shuffle(items)
# >>> items
# [4, 1, 2, 3, 5, 6, 7]
# >>>

# 例子 实现验证码功能
# 查询ASCII码表
# >>> for i in range(255):
# ...     print(i, chr(i))
# ...
# 48-57 对应 0-9
# 65-90 对应 A-Z
# 97-122 对应 a-z


idcode = ''
for i in range(1000):
    index = random.randint(1, 3)
    if index == 1:
        tmp = chr(random.randint(48, 57))
    elif index == 2:
        tmp = chr(random.randint(65, 90))
    else:
        tmp = chr(random.randint(97, 122))
    idcode += tmp
print(idcode)


