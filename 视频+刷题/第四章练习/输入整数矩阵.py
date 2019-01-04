"""
输入3X4整数矩阵，输出第2行第2列的元素，第3行第4列的元素。
【输入形式】
3行。每一行有4列，元素之间用空格隔开。
【输出形式】
两行。第一行是第2行第2列的元素值。第二行是第3行第4列的元素值。
【样例输入】
1 2 3 4
5 6 7 8
9 10 11 12
【样例输出】
6
12
"""

# str_list = []
int_total_list = []

for i in range(3):
    line = input().split()
    # str_list.append(line)
    int_list = []
    for j in line:
        j = int(j)
        int_list.append(j)
    int_total_list.append(int_list)
# print(int_total_list)
# [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12']]

# 输出：两行。第一行是第2行第2列的元素值。第二行是第3行第4列的元素值。
print(int_total_list[1][1])
print(int_total_list[2][3])