file = open("D:\The second\大三上学期\python\大作业5 标准普尔500预测-修订\大作业5 标准普尔500预测\股票.csv")
# print(file.readlines()[0])  # Date,Open,High,Low,Close,Volume,Adj Close
# print(type(file.readlines()))
content = file.readlines()[1:][::-1]

dic = {}
for line in content:
    # print(line.strip().split(","))
    line = line.strip().split(",")
    # print(line)
    key = line[0]
    dic[key] = [float(line[1]), float(line[4])]

list1 = list(dic.items())
# print(list1)

n = 0
m = 13

date_cha = {}
while m <= len(content):
    new_list = list1[n:m]
    date_list = [new_list[0][0], new_list[-1][0]]

    cha = float(new_list[0][1][0]) - float(new_list[-1][1][1])
    str_cha = "%0.2f" % cha
    date_cha[float(str_cha)] = date_list
    n += 13
    m += 13

# print(date_cha)
list3 = list(date_cha.items())
# print(list3)
def get_sort1(x):
    return abs(x[0])
list3 = sorted(list3, key=get_sort1, reverse=True)
# 变化最大以及相对应的起末日期
print("变化最大的前10个以及相对应的起末日期：")
# print(list3[:10])
for a, b in list3[:10]:
    print(a, b[0], b[1])

print("变化最小前10个以及相对应的起末日期：")
# print(list3[-10:])
for c, d in list3[::-1][:10]:
    print(c, d[0], d[1])
