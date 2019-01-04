a = [11, 22, 33, 44, 11, 22, 33, 44]
b = {11, 22, 33, 11, 12, 13}  # 可表列表也可表集合

# 可创一个新列表
c = []
for i in a:
    if i not in c:
        c.append(i)
print(c)

# 没有该方法

'''
d = {}
for j in b:
    if j not in d:
        d.append(j)
print(d)

'''

# 列表去重方法, 集合没有重复元素的， 可以将列表变成集合再转回列表
f = set(a)
print(f)
e = list(f)
print(e)

