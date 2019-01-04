# -*- coding: utf-8 -*-

'''
【问题描述】编写一个程序：将输入的一个N进制整数转换成M进制数（N和M在2到16进制之间），
            要求：N进制数和M进制数均以字符串方式存储。
【输入形式】输入的第一行、第二行分别表示N和M的值，第三行表示需要转换的数值k。
【输出形式】输出的一行为k转换后的结果（超过10的数值依次用大写字母ABCDEF表示，A表示11， B表示12，依次类推），
若输入的进制数值不合法（如：N和M没有落在2到16之间，或数据含有指定进制的非法字符（如：N=2时，k为12）），输出"illegal input"。
【样例输入】
2
16
11000011
【样例输出】
C3
'''


# n为待转十进制数，x为目标进制
def f(n, x):
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    b = []
    while True:
        s = n // x
        # print(s)
        y = n % x
        b.append(y)
        if s == 0:
            break
        n = s
    b.reverse()
    print(b)
    c = []
    for i in range(len(b)):
        c.append(a[b[i]])
    return c


N = int(input())
M = int(input())
try:
    if N >= 2 and N <= 16 and M >= 2 and M <= 16:
        x = int(input(), N)  # 转化为十进制
        # print(x)  # 195
        c = f(x, M)  # 调用函数
        for i in range(0, len(c)):
            print(c[i], end='')

    else:
        print('illegal input')
except:
    print('illegal input')
