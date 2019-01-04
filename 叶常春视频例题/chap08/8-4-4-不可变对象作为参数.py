# 例8-4-4  不可变对象作为参数
# 不可变对象作为参数。修改参数变量的值，不会影响到调用方。
import math  # 引入math模块，其内有大量数学计算函数


def square_root(x, y):
    x = x * x
    y = y * y
    return math.sqrt(x + y)  # 调用math模块内的sqrt函数求平方根


a = 3.0
b = 4.0
print("3.0和4.0的平方和：", square_root(a, b))
# a, b的值不会因x, y的改变而改变
print("a=", a)
print("b=", b)
