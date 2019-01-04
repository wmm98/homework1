# 例6-2-1  数字计数
# 程序功能：
#  输入一组整数，比如3 2 55 2 3 1 9，求各个数字出现的次数。所给出的例子中，3出现2次，2出现2次，其余各1次。

# 步骤1. 输入一组整数
num_line = input("在一行中输入一组整数（用空格隔开）：")
num_strs = num_line.split()  # 以空格为界，分离字符串，得到数字字符串的列表
# 转换成数字列表
num_list = []
for s in num_strs:
    num_list.append(int(s))

# 步骤2. 统计每个整数的出现次数
num_dict = {}
for n in num_list:
    if n in num_dict:
        num_dict[n] = num_dict[n] + 1
    else:
        num_dict[n] = 1

# 步骤3. 输出各数字出现次数
print("各数字出现次数：")
for key, value in num_dict.items():
    print(key, ':', value, '次')
