import random

player = int(input("请输入  (0)剪刀   (1)石头   (2)布"))
print("用户输入的是: ", player)

# 随机出一个数字, [0,2]
# 使用随机数函数 random
# random.randint(a,b), 能够生成[a,b]的随机整数
computer = random.randint(0, 2)
print("电脑输入的是: ", computer)

if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("player wins")
elif player == computer:
    print("equality")
else:
    print("computer wins")

# 三元表达式 if ... else 的简写
num1 = int(input())
num2 = int(input())

x = num1 if num1 > num2 else num2  # x取大的值
print(x)
