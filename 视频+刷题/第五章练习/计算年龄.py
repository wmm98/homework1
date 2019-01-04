'''【问题描述】编写一个程序，用户输入出生日期和当前日期，计算出实际年龄。
【输入形式】用户在第一行输入出生日期，在第二行输入当前日期。日期格式为年.月.日，即中间用.分割。
【输出形式】程序在下一行输出实际年龄。
【样例输入】
1964.2.19 
2001.7.21   
【样例输出】37
【样例说明】用户第一次输入的日期为出生日期，回车表示本次输入结束。第二次输入的为当前日期，回车表示本次输入结束。系统返回实际年龄'''

year1, month1, day1 = input().split(".")
year2, month2, day2 = input().split(".")

year1 = int(year1)
month1 = int(month1)
day1 = int(day1)

year2 = int(year2)
month2 = int(month2)
day2 = int(day2)

if month1 < month2:
    age = year2 - year1
elif month1 == month2:
    if day2 >= day1:
        age = year2 - year1
    else:
        age = year2 - year1 - 1
else:
    age = year2 - year1 - 1

print(age)