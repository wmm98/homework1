def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def year_days(year):
    '''得出year年是多少天'''
    if is_leap_year(year):
        return 366
    else:
        return 365

def what_day(year, month, date):
    day_delta = delta_days(year, month, date)
    #1980.1.1是星期二
    result_day = (day_delta + 2) % 7
    day_dict = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednseday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    return day_dict[result_day]


def delta_days(year, month, date):
    day_num = 0
    for y in range(1981, year + 1):
        day_num += year_days(y - 1)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for m in range(1, month):
        day_num += month_days[m - 1]
    if month > 2 and is_leap_year(year):
        day_num += 1
    day_num += date
    day_delta = day_num - 1  # 与1980.1.1相差多少天
    return day_delta

year, month, date = [int(x) for x in input().split('-')]
print(what_day(year, month, date))

# assert(is_leap_year(1980))
# assert(not is_leap_year(1990))
# assert(not is_leap_year(2100))
# assert(not is_leap_year(2122))
# assert(is_leap_year(1984))
# assert(not is_leap_year(2500))

# print(delta_days(1981, 1, 1))
# assert(delta_days(1980, 1, 1) == 0)
# assert(delta_days(1980, 1, 2) == 1)
# assert(delta_days(1981, 1, 1) == 366)
# assert(delta_days(1982, 1, 1) == 366 + 365)
# assert(delta_days(2004, 1, 6) == 8771)
# assert(delta_days(2500, 1, 1) == 189927)
# assert(delta_days(2500, 2, 1) == 189927 + 31)
# assert(delta_days(2500, 3, 1) == 189927 + 31 + 28)
# assert(delta_days(2500, 4, 1) == 189927 + 31 + 28 + 31)
# print("1980-1-1 => 2500.4.29", delta_days(2500, 4, 29))
# assert(delta_days(2500, 4, 29) == 190045)


# print("1980-1-1:", what_day(1980, 1, 1))
# print("1980-1-2:", what_day(1980, 1, 2))
# print("1980-1-8:", what_day(1980, 1, 8))
# print("2004-1-6:", what_day(2004, 1, 6))
# print("2008-2-29", what_day(2008, 2, 29))
# print("2500-4-29", what_day(2500, 4, 29))