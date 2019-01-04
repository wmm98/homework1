# 元组是不可变有序的元素的组合
# 元组的元素可以是任何类型的

# 列表转为元组
l = [1, 2, 3, "you"]
result = tuple(l)
print(result)  # (1, 2, 3, 'you')

# 元组的乘法  和列表的一样
t = (1, 2)
result = t * 2
print(result)  # (1, 2, 1, 2)

# 元组也可以相加

# 元组的拆包
a, b = (10, 20)
print(a, b)  # 10 20

# 交换两个数也可以用元组
c = 10
d = 21
c, d = (d, c)
print(c, d)  # 21 10