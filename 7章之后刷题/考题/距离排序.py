'''【描述】

给出三维空间中的n个点（不超过10个）,求出n个点两两之间的距离,并按距离由大到小依次输出两个点的坐标及它们之间的距离。

【输入】

输入包括两行，第一行包含一个整数n表示点的个数，第二行包含每个点的坐标(坐标都是整数)。
点的坐标的范围是0到100，输入数据中不存在坐标相同的点。

【输出】

对于大小为n的输入数据，输出n*(n-1)/2行格式如下的距离信息：
(x1,y1,z1)-(x2,y2,z2)=距离
其中距离保留到数点后面2位。


【样例输入】

4
0 0 0 1 0 0 1 1 0 1 1 1
【样例输出】

(0,0,0)-(1,1,1)=1.73
(0,0,0)-(1,1,0)=1.41
(1,0,0)-(1,1,1)=1.41
(0,0,0)-(1,0,0)=1.00
(1,0,0)-(1,1,0)=1.00
(1,1,0)-(1,1,1)=1.00
【提示】



1. 对于一行输出中的两个点(x1,y1,z1)和(x2,y2,z2)，点(x1,y1,z1)在输入数据中应出现在点(x2,y2,z2)的前面。

比如输入：
2
0 0 0 1 1 1
输出是：
(0,0,0)-(1,1,1)=1.73
但是如果输入：
2
1 1 1 0 0 0
输出应该是：
(1,1,1)-(0,0,0)=1.73


2. 如果有两对点p1,p2和p3,p4的距离相同，则先输出在输入数据中靠前的点对。

比如输入：
3
0 0 0 0 0 1 0 0 2
输出是：
(0,0,0)-(0,0,2)=2.00
(0,0,0)-(0,0,1)=1.00
(0,0,1)-(0,0,2)=1.00
如果输入变成：
3
0 0 2 0 0 1 0 0 0
则输出应该是：
(0,0,2)-(0,0,0)=2.00
(0,0,2)-(0,0,1)=1.00
(0,0,1)-(0,0,0)=1.00
'''
import math
n = int(input())
num = [int(i) for i in input().split()]
list1 = []
for i in range(n):
    s = []
    for j in range(3):
        s.append(num[i * 3 + j])
    list1.append(tuple(s))

list2 = []
flag = 1
for a in list1:
    for b in list1[flag:n]:
        distance = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)
        distance = "%.2f" % distance
        str1 = "(%d,%d,%d)%s(%d,%d,%d)%s%s" % (a[0], a[1], a[2], "-", b[0], b[1], b[2], "=", distance)
        list2.append([str1, float(distance)])
    flag += 1

def get_sort(x):
    return x[1]
l = sorted(list2, key=get_sort, reverse=True)

for r, s in l:
    print(r)


