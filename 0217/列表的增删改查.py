# 操作列表, 一般包括 增删改查

heroes = ['镜', '嬴政', '露娜', '娜可露露']

# 添加元素的方法
# append
heroes.append('黄忠')
print(heroes)  # 在列表最后面追加

# insert(index, object) 在指定位置插入
heroes.insert(1, '小乔')
print(heroes)
newHeroes = ['狄仁杰', '王昭君']

# extend(iterable) 添加可迭代对象
heroes.extend(newHeroes)
print(heroes)

# 删除元素 pop
print(heroes)  # ['镜', '小乔', '嬴政', '露娜', '娜可露露', '黄忠', '狄仁杰', '王昭君']
x = heroes.pop()  # 删除并返回
print(x)  # 王昭君
x = heroes.pop(2)  # 删除指定下标的元素
print(x)  # 嬴政
print(heroes)  # ['镜', '小乔', '露娜', '娜可露露', '黄忠', '狄仁杰']

# remove
heroes.remove('小乔')  # 删除不存在的会报错
print(heroes)  # ['镜', '露娜', '娜可露露', '黄忠', '狄仁杰']

# del关键字 这个功能强大, 列表删除少用
del heroes[2]
print(heroes)  # ['镜', '露娜', '黄忠', '狄仁杰']

# clear
heroes.clear()
print(heroes)  # []

# 查询
heroes = ['镜', '小乔', '镜', '露娜', '娜可露露', '黄忠', '狄仁杰']
print(heroes.index('镜'))  # 返回下标, 不存在元素报错
print(heroes.count('镜'))  # 2, 返回个数

# in 运算符
flag = '小乔' in heroes
print(flag)  # True

# 修改元素, 使用下标直接修改
heroes[1] = '镜'
print(heroes)  # ['镜', '镜', '镜', '露娜', '娜可露露', '黄忠', '狄仁杰']
