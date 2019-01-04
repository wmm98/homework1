'''


【输入形式】
从标准输入读取两行以空格分隔的整数，格式如下：

Ax1 Ay1 Ax2 Ay2
Bx1 By1 Bx2 By2

其中（x1，y1）和（x2，y2）为矩形对角线上端点的坐标。各坐标值均为整数，取值在0至1000之间。
 
【输出形式】

向标准输出打印一个整数，是两矩形相交部分的面积（可能为0）。

【输入样例】

0 0 2 2
1 1 3 4
 
【输出样例】
1

【提示】
输入的两点可以是矩形任一对角线上的端点，求相交的面积可以先求矩形在X轴和Y轴上的交集。
矩形在X轴上的交集可以按照如下算法进行求解：假设AX1和AX2中的较大值为MAX_AX，较小值为MIN_AX；
BX1和BX2中的较大值为MAX_BX，较小值为MIN_BX。用MAX_AX和MAX_BX中的较小者减去MIN_AX和MIN_BX中的较大者，
结果为正表示两矩形在X轴上的交集，若为负则表示不相交。

 
 	
'''
#
# x1, y1, x2, y2 = input().split()
# a1, b1, a2, b2 = input().split()
#
#
# x1 = int(x1)
# y1 = int(y1)
# x2 = int(x2)
# y2 = int(y2)
#
# a1 = int(a1)
# b1 = int(b1)
# a2 = int(a2)
# b2 = int(b2)
#
# max_x = max(x1, x2)
# min_x = min(x1, x2)
# max_y = max(y1, y2)
# min_y = min(y1, y2)
# max_a = max(a1, a2)
# min_a = min(a1, a2)
# max_b = max(b1, b2)
# min_b = min(b1, b2)
#
#
# if min(max_x, max_a) - max(min_a, min_x) > 0 and (min(max_y, max_b) - max(min_b, min_y)) > 0:
#     print(min(max_x, max_a) - max(min_a, min_x) * (min(max_y, max_b) - max(min_b, min_y)))
# else:
#     print(0)

# 输入的两点可以是矩形任一对角线上的端点，求相交的面积可以先求矩形在X轴和Y轴上的交集。
# 矩形在X轴上的交集可以按照如下算法进行求解：假设AX1和AX2中的较大值为MAX_AX，较小值为MIN_AX；
# BX1和BX2中的较大值为MAX_BX，较小值为MIN_BX。用MAX_AX和MAX_BX中的较小者减去MIN_AX和MIN_BX中的较大者，
# 结果为正表示两矩形在X轴上的交集，若为负则表示不相交。

pointA = [int(n) for n in input().split()]
pointB = [int(n) for n in input().split()]
MAX_AX = (pointA[0] if (pointA[0] > pointA[2])else pointA[2])
MIN_AX = (pointA[0] if (pointA[0] < pointA[2])else pointA[2])
MAX_BX = (pointB[0] if (pointB[0] > pointB[2])else pointB[2])
MIN_BX = (pointB[0] if (pointB[0] < pointB[2])else pointB[2])
x1 = (MAX_AX if (MAX_AX < MAX_BX)else MAX_BX)
x2 = (MIN_AX if (MIN_AX > MIN_BX)else MIN_BX)
x = x1 - x2

MAX_AY = (pointA[1] if (pointA[1] > pointA[3])else pointA[3])
MIN_AY = (pointA[1] if (pointA[1] < pointA[3])else pointA[3])
MAX_BY = (pointB[1] if (pointB[1] > pointB[3])else pointB[3])
MIN_BY = (pointB[1] if (pointB[1] < pointB[3])else pointB[3])
y1 = (MAX_AY if (MAX_AY < MAX_BY)else MAX_BY)
y2 = (MIN_AY if (MIN_AY > MIN_BY)else MIN_BY)
y = y1 - y2
if x <= 0 or y <= 0:
    print(0)
else:
    print(x * y)





