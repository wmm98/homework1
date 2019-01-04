

# 生成一个列表，从1到10

list = [i for i in range(1, 11)]
print(list)

# 打印偶数
list1 = [i for i in range(1, 11) if i % 2 == 0]
print(list1)


list2 = [2 for i in range(1, 11)]
# 输出10个2，第一个i表示输出的数字，后面的for循环表示循环的次数
print(list2)

list3 = [i for i in range(3) for j in range(2)]
print(list3)

list4 = [(i, j) for i in range(3) for j in range(2)]
print(list4)
# 表示i循环嵌套j循环