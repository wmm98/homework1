import time

# 时间戳
# result1 = time.time()
# print(result)  # 时间戳  1538794070.856156
#
# # 表示今年年份
# result1 = result / (24 * 60 * 60 * 365) + 1970
# print(result1)  # 2018.7948477344014


#
# # 时间元组
# # 获取方式：
# # import time
# # result = time.localtime([seconds]) seconds可表示默认的时间或者可选的时间戳
# result1 = time.time()
# result = time.localtime(result1)
# print(result)
# # time.struct_time(tm_year=2018, tm_mon=10, tm_mday=6,
# # tm_hour=10, tm_min=54, tm_sec=26, tm_wday=5, tm_yday=279, tm_isdst=0)
# # tm_yday=279, tm_isdst=0 分别表示一年中的第几天还是时令
# # -1 0 1 -1 决定是否为夏令时的标志


# 获取格式化的时间1
# import time
# 秒--> 可读时间
# time.ctime([seconds])
# seconds  可选的时间或者默认当前时间戳

# t = time.time()
# result1 = time.ctime(t)
# print(result1)  # Sat Oct  6 11:27:06 2018



# 获取格式化的时间2
# 时间元组 --> 可读时间
# import time
# time.asctime([p_tuple])
#    p_tuple 可选的时间元组或默认当前时间元组

# t = time.time()
# time_tupe = time.localtime()  # 不写就默认
# result1 = time.asctime(time_tupe)
# print(result1)




# 字符串 --> 格式化日期
# time.strftime(格式字符串，时间元组)
# 例如：
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# # 2018-10-06 11:39:05
#
# print(time.strftime("%y-%m-%d %H:%M:%S", time.localtime()))
# # 18-10-06 11:39:39
#
# print(time.strftime("%y.%m.%d %H:%M:%S", time.localtime()))
# # 18.10.06 11:40:09


# 格式化日期字符串改为时间元组
# t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
result = time.strptime("2018-10-06 11:39:05", "%Y-%m-%d %H:%M:%S")
print(result)
# time.struct_time(tm_year=2018, tm_mon=10, tm_mday=6, tm_hour=11, tm_min=39, tm_sec=5,
#  tm_wday=5, tm_yday=279, tm_isdst=-1)


t1 = time.mktime(result)  # 时间元组转为时间戳
print(t1)  # 1538797145.0