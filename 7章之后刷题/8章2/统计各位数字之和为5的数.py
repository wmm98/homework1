'''【问题描述】下面的函数count统计m和n（m和n都是3位数）之间（包含m和n本身）有多少个数其各位数字之和是5，并将统计结果 返回。
【输入形式】两个整数 m n
【输出形式】m和n之间各位数字之和为5的所有整数的个数
【样例输入】100 200
【样例输出】5'''

def count(x, y):
    flag = 0
    for i in range(x, y + 1):
        i = str(i)
        i_list = []
        for j in i:
            i_list.append(int(j))
        if sum(i_list) == 5:
            flag += 1
    return flag

m, n = input().split()
m = int(m)
n = int(n)
print(count(m, n))