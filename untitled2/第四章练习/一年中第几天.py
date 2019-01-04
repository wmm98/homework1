''' 
输入某年某月某日，判断这一天是这一年的第几天？程序分析：以3月5日为例，应该先把前两个月的加起来，
然后再加上5天即本年的第几天。特殊情况：闰年且输入月份大于3时需考虑多加一天。
提示：(1) 闰年的2月有29天，平年的2月有28天；
      (2) 如果年份满足以下两个条件之一，则该年就是闰年。
         i) 年份能被4整除且不能被100整除
         ii) 年份能被400整除

【输入形式】

输入一行，一行三个整数，用空格隔开，分别代表年月日。如2012 2 7  

代表2012年2月7日。注意，不要输入任何汉字。

【输出形式】

输出只有一个数字，即所对应的日期是该年的第几天。

【样例输入】

2012 1 1

【样例输出】
1
'''
# 求一年中的第几天
year, month, day = input().split()
year = int(year)
month = int(month)
day = int(day)

run_nian = [31, 29, 31, 30, 31, 30, 31, 31, 31, 30, 31, 30]
ping_nian = [31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 31, 30]
sum = 0
# sum1 = 0

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    run_nian1 = run_nian[:(month-1)]
    for i in run_nian1:
        sum += i
    print(sum + day)

else:
    ping_nian1 = ping_nian[:(month - 1)]
    for j in ping_nian1:
        sum += j
    print(sum + day)



