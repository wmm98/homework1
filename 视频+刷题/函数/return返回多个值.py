# 计算数字的和，差
def calculate(x, y):
    he = x + y
    cha = x - y
    return (he, cha)  # 当想返回多个数据的时候可以用集合的方式，列表，元组和集合都可以
he, cha = calculate(2, 3)  # 拆包方式
print(he, cha)

# 用下标方式表示
result = calculate(3, 4)
print(result[0], end=" ")
print(result[1])

# 5 -1
# 7 -1


