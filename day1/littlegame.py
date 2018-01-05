
# 猜年龄游戏

ageOfMe = 29
print(type(ageOfMe))
cGuess = int(input("Your guess:"))

if cGuess > ageOfMe:
    print("I am not that old.")
elif cGuess < ageOfMe:
    print("I am so happy.")
else:
    print("You got it.")
