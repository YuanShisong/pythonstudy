
# while循环


# count = 0
# while True:
#     print('''count:''' + str(count))
#     count += 1

# 重写猜年龄游戏
count = 0
ageOfMe = 29
while count < 3:
    cGuess = int(input("Your guess:"))
    if cGuess > ageOfMe:
        print("I am not that old.")
    elif cGuess < ageOfMe:
        print("I am so happy.")
    else:
        print("You got it.")
        break
    count += 1
else:
    print("You have tried too many times, piss off.")

'''
while 条件
    如果 while条件成立,则执行while里的逻辑
else 
    否则执行else中的逻辑
'''