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
all_info = []
if n <= 180:
    flag = 0
    for r in range(n):
        info = []
        name, m, d = input().split()
        if len(name) < 20:
            for i in name:
                if i.isspace():
                    flag += 1
        if flag < 1:
            info.append(name.title())
            info.append(int(m))
            info.append(int(d))
        all_info.append(info)
# print(all_info)



# 按名字排序
def getKeyName(x):
    return x[0]


name_list = sorted(all_info, key=getKeyName)


# 按名字长度排序
def getKeyNname_len(x):
    return len(x[0])


lenName_list = sorted(name_list, key=getKeyNname_len)


# 按月排序
def getKey_month(x):
    return x[1]


month_list = sorted(lenName_list, key=getKey_month)


# 按日排序
def getKey_day(x):
    return x[2]


day_list = sorted(month_list, key=getKey_day)

print(day_list)
# [['Tim', 3, 2], ['Bill', 3, 2], ['Avril', 3, 2], ['Candy', 4, 5], ['Sufia', 4, 5], ['Lagrange', 4, 5]]
result = []
# count = 0
# for i in range(len(day_list)):
#     for j in range(i + 1, len(day_list)):
#         if day_list[i][1] == day_list[j][1]:
#             count += 1
#             if day_list[i][1] not in result:
#                 result.append(day_list[i][1])
#
#             if day_list[i][2] not in result:
#                 result.append(day_list[i][2])
#             if day_list[i][0] not in result:
#                 result.append(day_list[i][0])
#             if day_list[j][0] not in result:
#                 result.append(day_list[j][0])
#
# print(result)
# # [3, 2, 'Tim', 'Bill', 'Avril', 4, 5, 'Candy', 'Sufia', 'Lagrange']
# if count == 0:
#     print("None")


