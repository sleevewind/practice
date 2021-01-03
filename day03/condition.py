# python 里的条件判断语句：if/ if else/ if elif elif else
# python 里不支持 switch case 语句
# age = int(input("请输入你的年龄："))
# if age < 18:
#     print('未满十八岁，禁止入内')
# else:
#     print("请进")

year = int(input('请输入年份'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year,'年是闰年',sep='')
else:
    print(year,'年不是闰年',sep='')