# 类型转换，将一个类型的数据转换为其他类型的数据
# 使用int内置类可以将数据转换为整数
age = input("请输入您的年龄：")
age = int(age)
print(age + 1)

x = '1a2c'
y = int(x, 16)  # 把数据转换成十六进制
print(y)  # 6700 默认十进制输出

# 使用float内置类可以将数据转换为浮点数
a = '12.34'
b = float(a)
print(b + 1)

# 使用str内置类可以将数据转换为浮点数
a = 34
b = str(34)

# 使用bool内置类可以将数据转换为浮点数
# 空元组，列表，字典，集合都是False
# 空字典: {}，空集合: set()
print(bool(-1))  # True
print(bool(0))  # False，只有0是False
print(bool('False'))  # True
print(bool(''))  # False
print(None)  # False

