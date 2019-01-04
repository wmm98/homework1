# 生成器是特殊的迭代器

l = (i for i in range(1, 1000000) if i % 2 == 0)
print(next(l))
print(next(l))
print(l.__next__())  # 作用等同print(next(l))
# 2
# 4
# 6

# # 也可以通过for遍历
# for j in l:
#     print(j)