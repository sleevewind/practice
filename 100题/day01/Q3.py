# With a given integral number n, write a program to generate
# a dictionary that contains (i, i x i) such that is an integral
# number between 1 and n (both included). and then the program
# should print the dictionary.Suppose the following input is
# supplied to the program: 8
#
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

import numpy as np
np.array()

n = int(input("please input the number:"))
# i = 0
# print('{', end='')
# for i in range(1, a):
#     print("{}:{}".format(i, i * i), end=',')
# i += 1
# print(i, ':', i * i, '}', sep='')

a = dict()
for i in range(1,n+1):
    a[i] = i*i
print(a)

# --------------------------------- #
a = {i: i * i for i in range(1, n + 1)}
print(a)