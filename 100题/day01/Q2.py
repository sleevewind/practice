# Write a program which can compute the factorial of a given
# numbers.The results should be printed in a comma-separated
# sequence on a single line.Suppose the following input is
# supplied to the program: 8 Then, the output should be:40320

x = int(input('请输入数字'))
ans = 1
while x != 1:
    ans = x * ans
    x -= 1
print(ans)

# ------------------------------------- #

x = int(input('请输入数字'))


def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


print(factorial(x))
