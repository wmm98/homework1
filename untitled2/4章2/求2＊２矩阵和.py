'''
【问题描述】输入A，B两个矩阵，规模为2*2，求出这两个整数矩阵相加的和

 【输入形式】 一共4行。前两行是矩阵A的元素，后两行是矩阵B的元素。

【输出形式】输出相加得到的结果矩阵。 同一行元素之间隔开一个空格。

【样例输入】

 1 1
 5 5
 
 7 7
 3 3
【样例输出】

 8 8
 8 8
 '''

int_total1 = []
for i in range(2):
    line = input().split()
    int_list1 = []
    for j in line:
        j = int(j)
        int_list1.append(j)
    int_total1.append(int_list1)
# print(int_total1)

int_total2 = []
for i in range(2):
    line = input().split()
    int_list2 = []
    for j in line:
        j = int(j)
        int_list2.append(j)
    int_total2.append(int_list2)
# print(int_total2)

result_list = []
for r in range(2):
    total_list = []
    for a in range(2):
        he = int_total1[r][a] + int_total2[r][a]
        total_list.append(he)
    result_list.append(total_list)
# print(result_list)


for b in range(2):
    print(result_list[b][0], result_list[b][1])