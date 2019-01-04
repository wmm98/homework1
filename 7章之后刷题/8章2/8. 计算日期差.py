# @Time    : 2018/4/3 9:38
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

def is_leap_year(year):
    '''year年是闰年吗'''
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def day_num_in_year(year, month, date):
    '''在year年里，month月date日是第几天'''
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        month_days[2] = 29

    day_num = date
    for m in range(month):
        day_num += month_days[m]
    return day_num

start_year, start_month, start_date = [int(x) for x in input().split()]
end_year, end_month, end_date = [int(x) for x in input().split()]

start_day_num = day_num_in_year(start_year, start_month, start_date)
end_day_num = day_num_in_year(end_year, end_month, end_date)

day_num_of_years = 0
for y in range(start_year, end_year):
    if is_leap_year(y):
        day_num_of_years += 366
    else:
        day_num_of_years += 365

delta_day_num = day_num_of_years + end_day_num - start_day_num
print(delta_day_num)
