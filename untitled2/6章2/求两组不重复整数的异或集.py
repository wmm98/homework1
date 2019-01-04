'''【问题描述】从标准输入中输入两组整数(每行不超过20个整数，每组整数中元素不重复),合并两组整数，去掉在两组整数中都出现的整数，
并按从小到大顺序排序输出（即两组整数集异或）。
【输入形式】首先输入第一组整数的个数，再输入第一组整数，以空格分隔；然后输入第二组整数的个数，再输入第二组整数，以空格分隔。
【输出形式】按从小到大顺序排序输出合并后的整数（去掉在两组整数中都出现的整数）。
【样例输入】
8
5 1 4 3 8 7 9 6 
4
5 2 8 10
【样例输出】
1 2 3 4 6 7 9 10
【样例说明】第一组整数个数为8，分别为5 1 4 3 8 7 9 6，第二组整数个数为4，分别为5 2 8 10。将第一组和第二组整数合并
（去掉在两组整数中都出现的整数），
并从小到大顺序排序后结果为1 2 3 4 6 7 9 10。'''

n = int(input())
first = [int(i) for i in input().split()]
n1 = int(input())
second = [int(j) for j in input().split()]
# print(first)
# print(second)
# first.extend(second)
# print(first)
if n1 <= 20 and n <= 20 and set(first).__len__() == n and set(second).__len__() == n1:

    z = set(first).symmetric_difference(set(second))
    # print(z)
    # first2 = second + first
    # # print(first2)
    # more = set(first2)
    # more1 = list(more)
    # l = sorted(more1)
    for r in z:
        print(r, end=" ")
# z = x.symmetric_difference(y)