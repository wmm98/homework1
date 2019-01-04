'''[【描述】

在一个有180人的大班级中，存在两个人生日相同的概率非常大，现给出每个学生的名字，出生月日。试找出所有生日相同的学生。


【输入】

第一行为整数n，表示有n个学生，n<=180。此后每行包含一个字符串和两个整数，分别表示学生的名字（名字第一个字母大写，其余小写，
不含空格，且长度小于20）和出生月(1<=m<= 12)日(1 <=d<=31)。名字、月、日之间用一个空格分隔

【输出】

每组生日相同的学生，输出一行，其中前两个数字表示月和日，后面跟着所有在当天出生的学生的名字，数字、名字之间都用一个空格分隔。
对所有的输出，要求按日期从前到后的顺序输出。 对生日相同的名字，按名字从短到长按序输出，长度相同的按字典序输出。
如果没有任何生日相同的学生，
输出：None  。

【样例输入】


【样例输出】
6
Avril 3 2
Candy 4 5
Tim 3 2
Sufia 4 5
Lagrange 4 5
Bill 3 2

3 2 Tim Bill Avril
4 5 Candy Sufia Lagrange
【样例说明】
样例输出中，3月2日有Tim, Bill, Avril三个人在当日出生。'''

n = int(input())
dateList = [[0 for j in range(2)] for i in range(n)]  # 是一个矩阵
nameList = [[0 for i in range(2)] for j in range(n)]


for n1 in range(n):
    line = input().split(" ", 1)
    nameList[n1][0] = line[0]
    nameList[n1][1] = line[1]
    month, day = line[1].split()
    dateList[n1][0] = int(month)
    dateList[n1][1] = int(day)
print(dateList)
print(nameList)
# [[3, 2], [4, 5], [3, 2], [4, 5], [4, 5], [3, 2]]
# [['Avril', '3 2'], ['Candy', '4 5'], ['Tim', '3 2'], ['Sufia', '4 5'], ['Lagrange', '4 5'], ['Bill', '3 2']]

# 按月日排序
def get_date(x):
    return (x[0], x[1])
sort_dateList = sorted(dateList, key=get_date)
# print(sort_dateList)
# [[3, 2], [3, 2], [3, 2], [4, 5], [4, 5], [4, 5]]

# 按姓名长度和字典顺序排序
def get_name(x):
    return (len(x[0]), x[0])

sort_nameList = sorted(nameList, key=get_name)
# print(sort_nameList)
# [['Tim', '3 2'], ['Bill', '3 2'], ['Avril', '3 2'], ['Candy', '4 5'], ['Sufia', '4 5'], ['Lagrange', '4 5']]

# 把sort_dateList的日期转成字符串格式并计算个数存在字典里
count_date = {}
for i in sort_dateList:
    str_date = "%s %s" % (i[0], i[1])
    if str_date not in count_date:
        d = {str_date: 1}
        count_date.update(d)
    else:
        count_date[str_date] += 1
# print(count_date)
# {'3 2': 3, '4 5': 3}

# 把次数大于一的的日期放在一个列表里面
date_list = []
for i, j in count_date.items():
    if j > 1:
        date_list.append(i)
# print(date_list)

# 用date_list索引sort_nameList
for i in date_list:
    print(i, end=" ")
    for j in sort_nameList:
        if i == j[1]:
            print(j[0], end=" ")
    print()

if len(date_list) == 0:
    print("None")


