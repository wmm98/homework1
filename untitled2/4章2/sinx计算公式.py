'''
已知sinx的近似计算公式如下：

 sin x = x - x3/3! + x5/5! - x7/7! + ... + (-1)n-1x2n-1/(2n-1)!

 其中x为弧度，n为正整数。编写程序根据用户输入的x和n的值，利用上述近似计算公式计算sinx的近似值，要求输出结果小数点后保留8位。

【输入形式】

从控制台输入小数x（0<=x<=20）和整数n（1<=n<=5000），两数中间用空格分隔。

【输出形式】

控制台输出公式结果：小数点后保留8位。

【样例输入1】

0.5236 4

【样例输出1】

0.50000105

【样例输入2】

0.5236  50

【样例输出2】

0.50000106

【样例说明】

输入x为0.5236，n为4，求得sinx近似计算公式的值为0.50000105，小数点后保留8位；同样，输入x为0.5236，n为50，
求得sinx近似计算公式的值为0.50000106，小数点后保留8位。
'''

# x, N = input().split()
# x = float(x)
# N = int(N)
# total = 0
# sinx = 0
#

# if 0 <= x <= 20 and 1 <= N <= 5000:
#     for n in range(2, N + 1):
#         result = 1
#         for j in range(1, 2 * n):
#             result *= j
#
#         sinx += (-1) ** (n - 1) * x ** (2 * n - 1) / result
#
#         # sin x = x - x3/3! + x5/5! - x7/7! + ... + (-1)n-1x2n-1/(2n-1)!
# total = sinx + x
# # print(result)
# print("%.8f" % total)

x, N = input().split()
x = float(x)
N = float(N)
total = 0.000
sinx = 0.000

# 先从第二位记起
if 0 <= x <= 20 and 2 <= N <= 5000:
    result = 1.000
    for n in range(2, int(N) + 1):
        for j in range(2 * n - 2, 2 * n):
            result *= j

        sinx += (-1) ** (n - 1) * x ** (2 * n - 1) / result

total = sinx + x
# print(result)
print("%.8f" % total)