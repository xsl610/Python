# 检查这个年份是否是闰年
year = int(input('输入年份：'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year, '是闰年')
else:
    print(year, '是平年')
