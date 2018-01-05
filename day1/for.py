
# for循环
for i in range(3):
    print('''loop:''' + str(i))

''' 字符串连接结果和,字符串连接是不一样的
loop:0
loop:1
loop:2
'''
# , 字符串后可以加其他类型
for i in range(3):
    print('loop:', i)

'''自动加空格
loop: 0
loop: 1
loop: 2
'''

# 打偶数
for i in range(0, 10, 2):
    print(i)

# 隔两个
for i in range(0, 10, 3):
    print(i)

#
target = 29
print("Welcome!!!")
tryAgain = 'yes'
while tryAgain == 'yes':
    for i in range(3):
        guess = int(input("Your guess:"))
        if guess == target:
            print(" You win!!!")
            break
        elif guess > target:
            print(" Try smaller...")
        else:
            print(" Try bigger")
    else:
        print(" You lose!!!")
    tryAgain = input(" start again???")
else:
    print(" Game Over!!!")
