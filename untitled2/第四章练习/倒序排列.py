'''
【输入形式】标准输入的前十行代表参与计算的十个整数。
【输出形式】标准输出的一行表示倒序后的数组，以空格作为间隔。
【样例输入】
1
2
3
4
5
6
7
8
9
10
【样例输出】
10 9 8 7 6 5 4 3 2 1
'''

i = 0
list = []
while i < 10:
    num = int(input())
    list.append(num)
    i += 1
list.sort(reverse=True)
for i in list:
    print(i, end=" ")