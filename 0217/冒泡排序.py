nums = [6, 5, 3, 1, 8, 7, 2, 4]

length = len(nums)
for i in range(0, length - 1):
    for j in range(0, length - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)
