# 例5-2-7
# 是闰年吗？
# 以下条件测试为真的话，是闰年：
#   年份year整除4，不被100整除；
#   或者year被400整除

year = int(input("输入年份："))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("闰年")
else:
    print("平年")
