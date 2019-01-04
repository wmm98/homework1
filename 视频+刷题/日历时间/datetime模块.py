import datetime

print(datetime.datetime.now())
print(datetime.datetime.today())
# 2018-10-06 15:27:56.725271
# 2018-10-06 15:27:56.725272  两两者都表示当前的时间

t = datetime.datetime.now()
print(type(t))  # <class 'datetime.datetime'>表示的是一个对象

print(t.year)
print(t.month)
print(t.day)
print(t.hour)
print(t.minute)
print(t.second)

# 2018
# 10
# 6
# 15
# 33
# 26