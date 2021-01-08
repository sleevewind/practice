i = 1
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(i, '*', j, '=', i * j, sep='', end='\t')
        i += 1
    j += 1
    print()
