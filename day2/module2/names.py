
#
names = 'liu guan zhang'
print(names[0])  # 结果为l 说明names为一个字符串

shu = ['liu', 'guan', 'zhang', 'zhao', 'kongming', 'huang', 'ma']
print(shu[0])
print(shu[1:3])  # ['guan', 'zhang'] [start；end)取头不取尾 左闭右开
print(shu[0:-1])  # 直接取所有
print(shu[0], shu[3])

print(shu[-1:-3])  # 结果:[] 故左侧值必须大于右侧值
print(shu[-3:-1])  # 结果:['kongming', 'huang']没有取到最后一个 符合左闭右开原则
print(shu[-3:])  # 结果:['kongming', 'huang', 'ma'] 取到最后一个

print(shu[:])  # 同样取所有

wei = ["cao", "zhangliao"]
wei.reverse()  # 反转
print(wei)
print(wei.index('cao'))
wei.append("dianwei")  # 追加到末尾
print(wei)
wei.insert(2, "xiahoudun")  # 指定位置插入
wei.sort()  # 排序
print(wei)
wei[0] ='caomengde'  # 替换
print(wei)
wei.remove('caomengde')  # 删除
print(wei)
wei.pop()  # pop最后一个
print(wei)
wei.pop(0)  # 指定下标pop
print(wei)
# print(wei.index("xiahouyuan"))  # ValueError: 'xiahouyuan' is not in list

print(wei.count('xiahoudun'))  # 统计

shu.extend(wei)  # 并集
print(shu)

del wei  # 删除变量
# print(wei)

print("========浅copy=========")
src = ['tang', 'sun',['haha', 'hehe'], 'zhu']
des = src.copy()
print(des)
src[2][0] = 1
print(src)
print(des)

print("========深copy=========")
import copy  # 引入copy模块
src = ['tang', 'sun',['haha', 'hehe'], 'zhu']
surface = src.copy()    # 浅copy
deep = copy.deepcopy(src)    # 深copy
print(surface)
src[2][0] = 1
print(src)
print(surface)
print(deep)  # ['tang', 'sun', ['haha', 'hehe'], 'zhu']

print("======Iterator======")
# 遍历列表
for i in src:
    print(i)

print("=====深层遍历=====")
for i in src:
    for j in i:
        print(j)

print("=====固定步长取值=====")


# print("=====固定步长取值=====")
# arr = []
# for i in range(100):
#     arr[i] = i + 1
# print(arr)
# for i in range(6):
#     print(arr[0,100,i])
