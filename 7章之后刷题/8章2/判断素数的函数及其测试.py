"""
【问题描述】
编写一个函数isprime(n)，判断整数n是否为素数。
测试此函数：从键盘输入一个整数，然后调用该函数进行判断，当为素数时，输出1，否则，输出0。

【输入形式】
从键盘输入一个整数。
【输出形式】
在屏幕上输出判断结果0或者1。
【输入样例】
45
【输出样例】
0
【样例说明】
45非素数，故输出为0。
 """

# 用户输入数字
num = int(input())

# 质数大于 1
if num > 1:
    # 查看因子
    for i in range(2, num):
        if (num % i) == 0:
            print(0)
            break
    else:
        print(1)

else:
    print(0)