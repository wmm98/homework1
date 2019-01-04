#例8-5-1  局部变量
import math    #引入math模块，其内有大量数学计算函数
def square_root(x, y):
    x = x * x
    y = y * y
    return math.sqrt(x + y)  #调用math模块内的sqrt函数求平方根

a = 3.0
b = 4.0
print("3.0和4.0的平方和：", square_root(a, b))
#函数外无法访问x, y
print("x=", x)
print("y=", y)
