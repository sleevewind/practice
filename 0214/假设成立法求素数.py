# 打印200以内质数
for i in range(2, 201):
    flag = True
    tmp = int(i ** 0.5)
    for j in range(2, tmp + 1):
        if i % j == 0:
            flag = False  # 是合数
            break
    if flag:
        print(i, '是质数')
