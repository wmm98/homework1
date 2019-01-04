# encoding=utf8


year = int(input())

# 以英里为单位
miles = 38241 * (year * 365 * 24) + 166.37 * 10 ** 8
# 以千米为单位
km = (38241 * (year * 365 * 24) + 166.37 * 10 ** 8) * 1.609344
# 一天文的单位计算
AU = miles / 92955887.6
# 无线返回时间
time = (km * 10 ** 3 / 299792458 / 3600) * 2

print("distance:")
print("%.2f %s" % (miles, 'miles'))
print("%.2f %s" % (km, 'km'))
print("%.2f %s" % (AU, 'AU'))
print("%s %.2f %s" % ("time:", time, 'hours'))