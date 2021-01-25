# sort()直接对列表排序
nums = [6, 5, 3, 1, 8, 7, 2, 4]
nums.sort()
print(nums)  # [1, 2, 3, 4, 5, 6, 7, 8]
nums.sort(reverse=True)
print(nums)  # [8, 7, 6, 5, 4, 3, 2, 1]

# sorted()内置函数, 返回新的列表, 不改变原来的列表
print(sorted(nums))  # [1, 2, 3, 4, 5, 6, 7, 8]

# reverse()
nums = [6, 5, 3, 1, 8, 7, 2, 4]
nums.reverse()
print(nums)  # [4, 2, 7, 8, 1, 3, 5, 6]
