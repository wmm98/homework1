# 集合是不可重复的，不能随机访问的，无序的元素的集合
# 集合里面的元素都是不可变类型的，列表是可变的就不可以为其元素
# 集合和元组字符串，列表都可有交集，跟使用[1,2,[1,2]]是不可行的。因为集合的元素是不可哈希的就不可迭代

# 设置一个空的集合的时候要用set()或者frozenset(),不可为{}，会被默认为一个空的字典
ss = set()
print(ss)  # set()
ss1 = {(1,), 3}
print(ss1)  # {3, (1,)}

# 列表去重的时候可以先转为集合再转为列表
list1 = [1, 2, 4, 5, 3, 2]
result = set(list1)
print(result)  # {1, 2, 3, 4, 5}
result1 = list(result)
print(result1)  # [1, 2, 3, 4, 5]


# 可变集合
s = {1, 2, 3, 4}
print(s, type(s))  # {1, 2, 3, 4} <class 'set'> 可变集合

s1 = "you"
s2 = set(s1)  # 里面可放可迭代对象，元组，列表，字符串都可以
print(s2, type(s2))  # {'u', 'y', 'o'} <class 'set'>
s3 = set((1, 2, 3))
print(s3, type(s3))  # {1, 2, 3} <class 'set'>

# 集合的推导式
s4 = {x + 1 for x in s}
print(s4, type(s4))  # {2, 3, 4, 5} <class 'set'>
s5 = set(x + 1 for x in s)
print(s5, type(s5))  # {2, 3, 4, 5} <class 'set'>


# 不可变结合,不可y用{}表示
a = frozenset("ouiowd")
print(a, type(a))  # frozenset({'u', 'w', 'o', 'd', 'i'}) <class 'frozenset'>
c = frozenset(x + 1 for x in range(0, 10))
print(c)  # frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
