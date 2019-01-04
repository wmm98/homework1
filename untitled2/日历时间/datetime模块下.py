import datetime

# 计算几天之后的日期

# 获取当前的时间
t = datetime.datetime.today()
result = t + datetime.timedelta(days=3)
print(result)  # 2018-10-09 15:46:16.817166  当前日期为6号

# 计算两天的时间
first = datetime.datetime(2018, 12, 9, 12, 00, 00)
second = datetime.datetime(2018, 12, 9, 10, 00, 00)
num = second - first
print(num)
# -1 day, 22:00:00

# 化为秒
second = num.total_seconds()
print(second)
