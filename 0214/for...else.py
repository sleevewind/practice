# 打印200以内质数
for i in range(2, 201):
    tmp = int(i ** 0.5)
    for j in range(2, tmp + 1):
        if i % j == 0:
            break
    else:  # for...else 当循环break没有执行的时候,执行else
        print(i, '是质数')
