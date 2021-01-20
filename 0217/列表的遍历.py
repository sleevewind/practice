# while 循环, for in循环
heroes = ['镜', '小乔', '露娜', '娜可露露', '黄忠', '狄仁杰']

for hero in heroes:
    print(hero, end=' ')

i = 0
while i < len(heroes):
    print(heroes[i], end=' ')
    i += 1

print()
a = 10
b = 13
# a = a + b
# b = a - b
# a = a - b

# a = a ^ b
# b = a ^ b
# a = a ^ b

a, b = b, a
print(a)  # 13
print(b)  # 10
