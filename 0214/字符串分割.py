# split rsplit splitlines partition rpartition
# split可以将一个str分割成list
x = '1,2,3,4,5,6,7'
x1 = x.split(',')
print(x1)  # ['1', '2', '3', '4', '5', '6', '7']

x2 = x.rsplit(',')
print(x2)  # ['1', '2', '3', '4', '5', '6', '7']
print(x.split(',', 2))  # ['1', '2', '3,4,5,6,7']
print(x.rsplit(',', 2))  # ['1,2,3,4,5', '6', '7']

# partition 指定一个字符串作为分隔符,分为三部分, 左边第一个
m = 'abcdefghijklmn'
print(m.partition('fgh'))  # ('abcde', 'fgh', 'ijklmn')元组类型

# rpartition 指定一个字符串作为分隔符,分为三部分, 右边第一个
m = '2020.2.14不要打开.MP4'
print(m.rpartition('.'))  # ('2020.2.14不要打开', '.', 'MP4')
