# 可以使用 % 占位符表示格式化字符串
name = 'Andrew'
age = 18
print('hello, I am ', name, ', ', age, ' years old', sep='')

# %s ==> 字符串占位符
# %d ==> 整数占位符
# %f ==> 浮点数占位符
print('hello, I am %s, %d years old, I earn $%f ' % (name, age, 3.14))

# %nd ==> 整数占位符
print('大家好, 我是%3d号男嘉宾' % 15)   #  15
print('大家好, 我是%03d号男嘉宾' % 15)  # 005
print('大家好, 我是%-3d号男嘉宾' % 15)  # 5

# %.nf ==> 小数点后n位
print('我今天挣了%.2f元钱' % 16.666666)  # 我今天挣了16.67元钱

# %x, %X
print(255) # 255
print('%x' % 255)  # ff
print('%X' % 255)  # FF

# %%
print('%%s %%d %d' % 16)  # %s %d 16
