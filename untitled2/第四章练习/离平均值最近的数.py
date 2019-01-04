"""
【问题描述】编程求一组数中离平均数最近的那个整数。计算位于前面的部分数的平均值，并返回离该平均值最近的那个数。
【输入形式】输入一行整数；最后一个是参与求平均的数的个数len。例如：1 2 3 4 5 6 7 10 12 13 8；意思是前面有10个数，最后的8是说前面8个数参与求平均，而不是10个数参与求平均。
【输出形式】离平均数最近的那个数。例如：5
【样例输入】1 2 3 4 5 6 7 10 12 13 8
【样例输出】5
"""

num = input().split()
list = []
for j in num:
    j = int(j)
    list.append(j)
# print(list)

num1 = num[0:(int(num[len(num) - 1]))]
# print(num1)
sum = 0
for i in num1:
    i = int(i)
    sum += i
# print(sum)
avg = sum / len(num1)
# print(avg)


# print(list)

if avg in list:
    print(avg)
else:
    list.append(avg)
    list.sort()
    # print(list.index(avg))
    if(list[list.index(avg)] - list[list.index(avg) - 1]) > (list[list.index(avg) + 1] - list[list.index(avg)]):
        print(list[list.index(avg) + 1])
    else:
        print(list[list.index(avg) - 1])



