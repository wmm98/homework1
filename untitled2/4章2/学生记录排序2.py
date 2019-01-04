# 【问题描述】
# 从键盘中读入最多不超过50个学生的学生信息（包括空格隔开的姓名、学号、年龄信息，以学号从低到高排序）
# 【输入形式】
# 每次键盘读入最多不超过50个学生的学生信息：
# 第一行为学生人数；
# 后面每一行为空格隔开的学生学号、姓名、年龄，其中学号和年龄都是整数。
# 【输出形式】
# 分别以姓名顺序（从低到高）和年龄顺序（从低到高）将学生信息输出，每行输出一位学生的信息，其中学号占3位，
# 姓名（英文）占6位，年龄占3位，均为右对齐。年龄相同时按姓名从低到高排序。两种顺序的输出结果用一行空行相隔。
# 【输入样例】
# 4
'''
1 aaa 22
45 bbb 23
54 ddd 20
110 ccc 19
'''

# 【输出样例】
#      1    aaa     22
#   45     bbb     23
# 110     ccc     19
#   54     ddd     20
#
# 110     ccc     19
#   54     ddd     20
#     1     aaa     22
#   45     bbb     23
# 【样例说明】
# 从键盘输入四个学生记录，分别按姓名和年龄排序并输出。

n = int(input())
info_list = []
if n <= 50:
    for r in range(n):
        info = input().split()
        info_list.append(info)
print(info_list)

# 按年龄排序
sort_list = []
for i in range(n):
    min_age = 0
    for j in range(i + 1, n):
        min_age = min(int(info_list[i][2]), int(info_list[j][2]))


        # if int(info_list[i][2]) < int(info_list[j][2]):
        #     sort_list.append(info_list[i])
        # elif int(info_list[i][2]) > int(info_list[j][2]):
        #     sort_list.append(info_list[j])
        # else:
        #     if info_list[i][1] > info_list[j][1]:
        #         sort_list.append(info_list[i])
        #     else:
        #         sort_list.append(info_list[j])
print(sort_list)