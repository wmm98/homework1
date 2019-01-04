# 直接加起来
str = " yoiu" + "uoiui"
print(str)

# 直接空格，两个字符串要始终在同一行上
str1 = " yoiu"     "uoiui"
print(str1)

# 直接填补
result = "yoiui%s" % "123"
print(result)

result1 = "youi%s%d" %("123", 345)

# 字符串的乘法
end = "abc\t" * 10
print(end)
# abc	abc	abc	abc	abc	abc	abc	abc	abc	abc