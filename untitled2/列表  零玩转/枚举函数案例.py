values = ["a", "b", "c", "o", "p"]

# 根据列表，创建一个枚举对象
# enumerate(values)
print(list(enumerate(values)))  # 将枚举对象转为列表
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'o'), (4, 'p')]

# 遍历枚举对象，枚举对象可以直接被遍历
for i, j in enumerate(values):
    print(i, j)

# 输出的结果
# 0 a
# 1 b
# 2 c
# 3 o
# 4 p

# 想让索引从别的数开始可以改变，如下
for i, j in enumerate(values, 1):
    print(i, j)
# 这样索引就是从1开始了
# 1 a
# 2 b
# 3 c
# 4 o
# 5 p

