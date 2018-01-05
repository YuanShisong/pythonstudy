'''
鸡汤：
    《追风筝的人》
    《白鹿原》
    《琳达看美国》
'''

# 列表 元组(不可变列表) 集合 字符串:不可修改

list1 = [1,9,2,3,2,4,5,3]
print(list1)
list1 = set(list1)
# 集合是有序的？？？ 官方文档:A set object is an unordered collection of distinct hashable objects.
print(list1)

set1 = set(['2','2','1','4','9','5'])
print(set1)
'''
无序的,不重复的,可哈希的对象集合，但为什么放数字就是有序的？？？
应该是和哈希算法有关, 数字小计算出的hash值就小？

set1 = set(['2','2','1','4','9','5'])
print(set1) # 三次输出结果如下
{'2', '5', '4', '9', '1'}
{'9', '4', '1', '2', '5'}
{'2', '9', '4', '1', '5'}

set2 = set([1,9,2,3,2,4,5,3])
print(set2) # 结果如下
{1, 2, 3, 4, 5, 9}
{1, 2, 3, 4, 5, 9}
'''

# set2 = set(['a', 'c', 'b', 'c', 'f', 'd', 'e'])
# print(set2)


'''取交集'''
set3 = set([1,9,2,3,4,5])
set4 = set([1,9,6,7])
print(set3.intersection(set4))  # {1, 9}

'''取并集'''
print(set3.union(set4))  # {1, 2, 3, 4, 5, 6, 7, 9}


'''取差集'''
print(set3.difference(set4))  # {2, 3, 4, 5} in set3 not in set4
print(set4.difference(set3))  # {6, 7} in set4 not in set3

'''子集'''
print(set4.issubset(set4))  # False
'''父集'''
print(set4.issuperset(set3))  # False
'''对称交集'''
print(set3.symmetric_difference(set4))  # {2, 3, 4, 5, 6, 7}

'''isdisjoint是否无交集，无交集返回True'''
set5 = set([8, 7])
print(set5.isdisjoint(set3))  # True
print(set5.isdisjoint(set4))  # False

'''用运算符方式表达'''
print(set3 & set4)  # {1, 9}
print(set3 | set4)  # {1, 2, 3, 4, 5, 6, 7, 9}
print(set3 > set4)
print(set3 >= set4)

set3.add(999)
print(set3)  # 确实无序

print(1 in set1)
print(1 in list1)

'''remove pop discard 区别
remove 删除指定元素 返回值为None 删除不存在的元素时会报错
pop 删除随机元素 返回值为被删除元素
discard 删除指定元素 返回值为None 删除不存在的元素时不会报错
'''
print('---------------------')
s6 = set([1,9,2,3,4,5])
s6.remove(1)
print(s6.remove(9))
print(s6)
# s6.remove(8)  # 删除不存在的元素时会报错 KeyError: 8

s7 = set([1,9,2,3,4,5])
print(s7.pop())
print(s7.pop())
print(s7.pop())
print(s7)

s8 = set([1,9,2,3,4,5])
print(s8.discard(8))
print(s8.discard(1))
print(s8)
# test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method # test fileno() method 