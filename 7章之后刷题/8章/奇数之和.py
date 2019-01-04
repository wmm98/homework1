"""
将1～p之间奇数顺序累加存入n中，直到其和首次等于或大于q为止或1～p之间所有奇数参与累加为止。
程序输入p,q的值，输出n的值、参与累加的奇数个数，以及参与运算的最大的那个奇数（分别占一行）。
【输入形式】

分两行输入p和q的值。
【输出形式】

依次输出n的值、参与累加的奇数个数，以及参与运算的最大的那个奇数
【样例输入】

1000
4000
【样例输出】

4096
64
127
"""


def sum(p, q):
    n = 0
    count = 0
    max_ji = 0
    for i in range(1, p + 1):
        if i % 2 != 0 and n < q:
            n += i
            count += 1
            if max_ji < i:
                max_ji = i

    return str(n) + "\n" + str(count) + "\n" + str(max_ji)


x = int(input())
y = int(input())
result = sum(x, y)
print(result)
