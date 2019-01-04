'''
输入n的值和n个数，进行排序并输出。
【输入形式】

首先输入整数个数n；

接着输入n个整数

【输出形式】

从小到大地输出n个整数
 【输入示例】

3

1  5 -10
'''


n = int(input())
num = input().split()
list = []
for j in num:
    j = int(j)
    list.append(j)


list.sort()
for r in list:
    print(r, end=' ')