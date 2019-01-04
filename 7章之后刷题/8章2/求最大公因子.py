'''
【问题描述】用递归方法编写求最大公因子程序。两个正整数x和y的最大公因子定义为：如果y<=x且x mod y＝0时，
gcd(x,y)=y;如果y>x时，gcd(x,y)=gcd(y,x);其他情况，gcd(x,y)=gcd(y,x mod y)。这里，x mod y是求x除以y的余数。
【输入形式】用户在第一行输入两个数字，数字之间用空格分割。
【输出形式】程序在下一行输出前面输入的两个数字的最大公因子。
【样例输入】36 24
【样例输出】12
【样例说明】用户输入36，24，程序输出它们的最大公因子12
'''


def hcf(x, y):
    """该函数返回两个数的最大公约数"""

    # 获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf

a, b = input().split()
result = hcf(int(a), int(b))
print(result)