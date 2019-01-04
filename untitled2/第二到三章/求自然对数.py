'''

编写程序，输入实数x，通过调用库函数求x的绝对值的平方根的自然对数(log)
【输入形式】

输入一个实数。
【输出形式】

输出计算后的结果。保留5位小数。
【样例输入】

-9
【样例输出】

1.09861

'''


import math
x = float(input())
x1 = abs(x)
y = math.sqrt(x1)
z = math.log(y)
print("%.5f" % z)
print("%.2f" % 0.625)
print("%.2f" % 0.626)
print("%.2f" % 0.6250)
print("%.2f" % 0.6251)
print(round(0.625, 2))
print(round(0.6251, 2))



