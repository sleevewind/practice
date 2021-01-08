x = 'abcdefghijklmna'

# 使用内置函数获取长度
print(len(x))

# 查找内容的相关方法, find/index/rfind/rindex
print(x.find('l'))  # 11 获取指定字符下标
print(x.index('l'))  # 11 获取指定字符下标
print(x.find('z'))  # 如果字符不存在, 返回-1
# print(x.index('z'))  # 如果字符不存在, 报错

print(x.find('j', 4, 10))  # 9 [start,end)
print(x.rfind('a'))  # 14 找最大的下标

# startswith, endswith
print('hello'.startswith('he'))  # True
print('hello'.endswith('lo'))  # True

print('123'.isdigit())  # True
print('3.14'.isdigit())  # False
print(x.count('a'))

# replace方法: 替换字符串
word = 'hello'
m = word.replace('l', 'x')
print(word)  # hello
print(word.replace('l', 'x'))  # hexxo
