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
    dic[key] = float(line[-1])

list1 = list(dic.items())
# print(list1)

n = 0
m = 13

date_cha = {}
while m <= len(content):
    new_list = list1[n:m]
    date_list = [new_list[0][0], new_list[-1][0]]

    # 排序
    def get_sort(x):
        return x[-1]
    final_list = sorted(new_list, key=get_sort, reverse=True)
    # print(final_list)
    cha = float(final_list[0][1]) - float(final_list[-1][1])
    str_cha = "%0.2f" % cha
    date_cha[float(str_cha)] = date_list
    n += 13
    m += 13

# print(date_cha)
list3 = list(date_cha.items())
def get_sort1(x):
    return x[0]
list3 = sorted(list3, key=get_sort1, reverse=True)
# 变化最大以及相对应的起末日期
print("变化最大以及相对应的起末日期：")
print(list3[0])
print("变化最小以及相对应的起末日期：")
print(list3[-1])
