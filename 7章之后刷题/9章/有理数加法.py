'''【问题描述】

定义有理数类，定义计算两个有理数的和的方法。程序输入两个有理数，输出它们的和。
【输入形式】

输入在一行中按照a1/b1 a2/b2的格式给出两个分数形式的有理数，其中分子和分母全是正整数。
【输出形式】

在一行中按照a/b的格式输出两个有理数的和。注意必须是该有理数的最简分数形式，若分母为1，则只输出分子。

【样例输入】

1/3 1/6
【样例输出】

1/2'''
from fractions import Fraction
class yl_shu:
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y

    def sum(self, x, y):
        return x + y
n, m = input().split()
n = Fraction(n)
m = Fraction(m)
result = yl_shu()
print(result.sum(n, m))

