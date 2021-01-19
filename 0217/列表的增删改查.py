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

# 删除元素 pop remove clear
print(heroes)