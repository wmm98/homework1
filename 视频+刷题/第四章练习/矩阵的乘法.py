"""【问题描述】
编写程序，完成3*４矩阵和4*３整数矩阵的乘法，输出结果矩阵。
【输入形式】
以先行后列顺序输入第一个矩阵，而后输入第二个矩阵。
【输出形式】
先行后列顺序输出结果矩阵，每个元素的显示宽度为8格，屏幕一行只显示矩阵的一行。
例如要计算如下两个矩阵
第一个矩阵            1 2 3 4

                     5 6 7 8

                     9 1 2 3

第二个矩阵            9 8 7

                     6 5 4

                     3 2 1

                     1 2 3

输入与输出格式如下
【样例输入】
1 2 3 4 5 6 7 8 9 1 2 3 9 8 7 6 5 4 3 2 1 1 2 3
【样例输出】

      34      32      30
      110     100     90
      96      87      78
"""


line = input().split()
int_list = []
for i in line:
    i = int(i)
    int_list.append(i)

int_total_list1 = []
for a in range(3):
    int_row = []
    for b in range(4):
        int_row.append(int_list[a * 4 + b])
    int_total_list1.append(int_row)
# print(int_row)
# print(int_total_list1)

int_total_list2 = []
for r in range(4):
    int_cow = []
    for c in range(3):
        int_cow.append(int_list[r * 3 + c + 12])
    int_total_list2.append(int_cow)
# print(int_total_list2)


# 最后生成一个3*3的矩阵
total_list = []
for i in range(3):
    list3 = []
    for j in range(3):
        ji = int_total_list1[i][0] * int_total_list2[0][j] + int_total_list1[i][1] * int_total_list2[1][j] + \
             int_total_list1[i][2] * int_total_list2[2][j] + int_total_list1[i][3] * int_total_list2[3][j]
        list3.append(ji)
    total_list.append(list3)
# print(total_list)

for i in range(3):
    print(str(total_list[i][0]).ljust(6), str(total_list[i][1]).ljust(6), str(total_list[i][2]).ljust(6))

# for r in range(3):
#     print(str(total_list[r][0]) + "\t", str(total_list[r][1]) + "\t", str(total_list[r][2]))