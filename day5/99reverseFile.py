
#
rvs = open('MakeMoreTime_reverseOrder.txt', 'r', encoding='utf-8')

rgt = open('MakeMoreTime.txt', 'w', encoding='utf-8')

# for i in rvs.readlines():
#     rgt.writelines(i)

# for i in rvs.readlines():
#     rgt.writelines(i)

con = rvs.readlines()
len = len(con)
for i in range(len):
    rgt.writelines(con[len - i - 1])


rvs.close()
rgt.close()