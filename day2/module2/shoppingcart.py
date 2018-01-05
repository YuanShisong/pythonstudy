'''
要求：
    1、启动程序，让用户输入工资，然后打印商品列表
    2、允许用户根据商品编码购买商品
    3、用户选择商品后，检测余额是否够，够就扣款，不够就提醒
    4、可随时退出，退出时，打印已购买商品和余额
'''

# items = ([1, 'IphoneX', 9000], [2, 'Mac Pro', 15000], [3, 'coffee', 32])
#
# salary = int(input("Your Salary:"))
# left = salary
# cart = []
# while True:
#     print('Available items:', items)
#     ipt = input("Please enter the NO. you wanna buy:")
#     num = -1;
#
#     if ipt == 'q' or ipt == 'quit':
#         break;
#     else:
#         num = int(ipt)
#     for item in items:
#         if(item[0] == num):
#             cost = item[2]
#             if left >= cost:
#                 cart.append(item)
#                 left = left - cost
#                 print(cart)
#                 print(left)
#             else:
#                 print("You don't have enough money, please choose a cheaper one:")
#         else:
#             continue
# print("What you bought:", cart)
# print("You've got:",left, "left, you spent:",(salary - left))
# print(items)

# 2.0版本
products = [
        ('Iphone', 9000),
        ('Coffee', 31),
        ('Mac Pro', 15000),
        ('clothes', 1000)
]  #商品列表
cart = []  #购物车
print("可买商品：")

# 输出商品列表
for i, pro in enumerate(products):
    print(i, pro)
# 输入工资
salary = input("输入工资：")
if salary.isdigit():
    salary = int(salary)
else:
    exit("工资输入有误,必须输入数字格式")

# 主逻辑
while True:
    ipt = input("选择要购买的商品编码, 或输入q结账退出:")
    if ipt.isdigit():
        num = int(ipt)
        if num < 0 or num > len(products) - 1:
            print("编码输入有误")
        else:
            for index, item in enumerate(products):
                if num == index:
                    if item[1] > salary:
                        print("买不起")
                    else:
                        salary = salary - item[1]
                        cart.append(item)
        # print("加购物车,减余额等操作")
    elif 'q' == ipt or 'quit' ==ipt:
        print("--------所剩余额:\033[31;1m%s\033[0m, 所购商品：---------" %(salary))
        for i, bt in enumerate(cart):
            print(i + 1, bt)
        exit()
    else:
        print("输入有误")














