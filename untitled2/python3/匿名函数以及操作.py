"""匿名函数不用返回，自带返回值，当写简单的计算
或编程的时候用匿名函数，否则用def函数"""

# 变量名 = lambda,参数，参数，参数：式子
sum = lambda a, b, c: a + b + c
result = sum(1, 1, 1)
print("result = %d" % result)
