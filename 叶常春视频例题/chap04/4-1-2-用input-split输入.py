# 例4-1-2  用input函数和split方法输入数据
# 输入一行字符串
line = input("输入多个整数，用空格隔开：")  # line是一个字符串
print("line=", line)
# 以空格为分隔符，分割字符串得到数字字符串列表
num_strs = line.split()  # num_strs是数字字符串列表
print("num_strs=", num_strs)

# 数字字符串列表转换为数字列表
nums = []
for s in num_strs:
    nums.append(int(s))
print("nums=", nums)

# 输入多个实数，用逗号隔开
line = input("输入多个实数，用逗号隔开:")
# 以逗号为分隔符，分割字符串得到数字字符串列表
fnum_strs = line.split(',')  # 分隔符是逗号，不是空格
fnums = []
for w in fnum_strs:
    fnums.append(float(w))
print("fnums=", fnums)

# 输入3个名字存入a, b, c
line = input("输入3个名字：")
# 3个元素的列表赋值给3个变量。
# 注意左边变量个数和列表元素的个数必须相等，否则报错。
a, b, c = line.split()
print(a)  # 输出a变量的值
print(b)
print(c)
