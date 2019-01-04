# 可变集合可以增删，不可改查
# 不可变集合都不可以
# 都可以通过迭代器，for循环今进行遍历

s = {1, 2, 3, 5}
# 生成有个迭代器
its = iter(s)
for i in its:
    print(i, end=" ")  # 1 2 3 5


for j in s:
    print(j, end=" ")  # 1 2 3 5