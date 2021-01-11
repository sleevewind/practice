# Ljust 字符串以指定长度显示, 默认在右边用空格补齐
# Ljust(width, fillchar)
print('Monday'.ljust(10, '*'))  # Monday****
print('Monday'.rjust(10, '*'))  # ****Monday
print('Monday'.center(10, '+'))  # ++Monday++

print('    apple    '.lstrip())  # 去掉左边空格
print('    apple    '.rstrip())  # 去掉右边空格
print('    apple    '.strip())  # 去掉两边空格
print('++++apple++++'.strip('+'))  # 去掉两边'+'

# 将字符串分割成列表
x = 'zhangsan,lisi,wangwu'
print(x.split(','))#['zhangsan', 'lisi', 'wangwu']
# 将列表转为字符串
fruits = ['apple', 'pear', 'peach', 'orange']
print('-'.join(fruits))  # apple-pear-peach-orange
