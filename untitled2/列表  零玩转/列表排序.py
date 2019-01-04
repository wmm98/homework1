s = [("a", 1), ("c", 3), ("b", 4), ("d", 5)]
s.sort()  # [('a', 1), ('b', 4), ('c', 3), ('d', 5)]  按照元组的第一个元素排序
print(s)


s1 = [("a", 1), ("c", 3), ("b", 4), ("d", 5)]
# 按照元组的第二个元素排序

def getKey(x):
    return x[1]

result = sorted(s1, key=getKey)  # [('a', 1), ('c', 3), ('b', 4), ('d', 5)]
print(result)

result1 = sorted(s1, key=getKey, reverse=True)  # [('d', 5), ('b', 4), ('c', 3), ('a', 1)] 降序
print(result1)

# sorted() 并不会改变列表的
# 对象.sort()会直接修改列表
str = "iouio"
result = sorted(str)
print(result)  # ['i', 'i', 'o', 'o', 'u']

# str.sort()
# print(str) sort() 会修改字符串的内容，而字符串是不可变的，所以会出现异常

s2 = [("a", 1), ("c", 3), ("b", 4), ("d", 5)]
s2.sort()
print(s2)  # [('a', 1), ('b', 4), ('c', 3), ('d', 5)]

# 按年龄排序
def getKey(x):
    return x[1]
s2.sort(key=getKey)
print(s2)  # [('a', 1), ('c', 3), ('b', 4), ('d', 5)]
s2.sort(key=getKey, reverse=True)
print(s2)  # [('d', 5), ('b', 4), ('c', 3), ('a', 1)]

