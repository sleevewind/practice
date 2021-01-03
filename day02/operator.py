# 在python3里，整数除法的结果是浮点数
# 在python2里，整数除法的结果是整数
print(6 / 2)  # 3.0
print(10 / 3)  # 3.3333333333333335
print(10 // 3)  # 整除运算，向下取整 3

# 幂运算
print(3 ** 3)
print(81 ** 0.5)

a = b = c = d = 10
print(a, b, c, d)

o, *p, q = 1, 2, 3, 4, 5, 6  # *p 代表可变长度
print(o, p, q)  # 1 [2, 3, 4, 5] 6

# 比较运算符在字符串里的使用
# 根据各个字符的编码值逐位比较
print('a' > 'b')  # False
print('abc' > 'b')  # False

# 逻辑运算符：and or not
print((3 > 2 and 5 > 4))  # True
print((3 > 2 or 5 > 3))  # True
print(not 3 > 2)  # false

# 逻辑与运算做取值时，取第一个为 False 的值；
# 如果所有运算数都是True，取最后一个值
a = 3 and 5 and 0 and 'hello'  # 0
b = 'good' and 'yes' and 'ok' and 100  # 100
print(a, b)

# 逻辑或运算做取值时，取第一个为 True 的值；
# 如果所有运算数都是False，取最后一个值
a = 0 or 0 or 3 or 'hello'  # 3
b = 0 or [] or {} or ()  # ()
print(a, b)

# 位运算符
# &(与) |(或) ^(异或) <<(左移) >>(右移) ~(取反)
a = 23
b= 14
print(a&b)
print(a|b)
print(a^b)
print(~a)
