# 下标又叫索引, 表示第几个数据
# 可迭代对象: str list tuple dict set range 可以遍历
# str list tuple 可以使用下标获取或操作数据
word = 'zhangsan'
print(word[4])
# 字符串是不可变数据类型
# word[4] = 'x' 报错

# 切片: 从字符串里复制一段指定内容, 生成一个新的字符串
m = 'abcdefghijklmn'
# str(start:end:step), [start end)左闭右开
print(m[2:9])  # cdefghi
print(m[2:])  # cdefghijklmn, 只设置start会直到最后
print(m[:9])  # abcdefghi, 只设置end会从头开始
print(m[2:9:2])  # cegi, step指步长, step不能为0
print(m[9:2:-1])  # jihgfed, step为负数, 从右往左找
print(m[-9:-2])  # fghijkl, 从右往左为负数 -9:f, -2:m
print(m[:])  # abcdefghijklmn, 从头到尾
print(m[::])  # abcdefghijklmn, 从头到尾
print(m[::-1])  # nmlkjihgfedcba, 从尾到头
