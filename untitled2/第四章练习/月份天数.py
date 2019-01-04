'''
【问题描述】

编写一个函数 day_of_month(year, month)

编写程序输入年(year)、月(month)，调用该函数，返回该年份该月的天数，输出返回的天数。

公历闰年的计算方法为：

    年份能被4整除且不能被100整除的为闰年

    或者，年份能被400整除的是闰年。



【输入描述】

共一行。有两个整数，第一个是年份，第二个是月份。年份和月份之间以一个空格隔开。

【输出描述】 

输出该年该月的天数。

【输入示例】

2017 11

【输出示例】

30
'''


def day_of_month(year1, month1):


    #  年份能被4整除且不能被100整除的为闰年 或者，年份能被400整除的是闰年。

    if (year % 4 == 0 and (year % 100 != 0)) or (year1 % 400 == 0):
        if 0 != (month1 % 2) or month == 8:
            print("31")
        elif month1 == 2:
            print("29")
        else:
            print("30")
    else:
        if 0 != (month1 % 2) or month == 8:
            print("31")
        elif month1 == 2:
            print("28")
        else:
            print("30")


year, month = input().split()
year = int(year)
month = int(month)
day_of_month(year, month)
