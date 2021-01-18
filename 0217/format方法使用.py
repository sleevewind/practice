# {} 进行占位
x = 'hello I am {}, {} years old'.format('Andrew', 23)
print(x)  # hello I am Andrew, 23 years old

# {下标}
y = 'hello I am {1}, {0} years old'.format(20, 'Jerry')
print(y)

# {变量名}
z = 'hello I am {name}, {age} years old, come from {addr}'.format(age=20, name='Jerry', addr='Beijing')
print(z)

m = ['zhangsan', 18, 'shanghai']
n = 'hello I am {}, {} years old, come from {}'.format(m[0], m[1], m[2])
print(n)  # hello I am zhangsan, 18 years old, come from shanghai
n = 'hello I am {}, {} years old, come from {}'.format(*m)
print(n)  # hello I am zhangsan, 18 years old, come from shanghai

q = {'name': 'zhangsan', 'age': 18, 'addr': 'shanghai'}
p = 'hello I am {name}, {age} years old, come from {addr}'.format(**q)
print(p)  # hello I am zhangsan, 18 years old, come from shanghai
