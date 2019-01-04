# 列表的增加
nums = [1, 2, 3, 5]
nums.append(0)
print(nums)  # [1, 2, 3, 5, 0]
nums.insert(0, 9)  # [9, 1, 2, 3, 5, 0]
print(nums)

# 列表的乘法
num = [1, 3]
print(num * 3)  # [1, 3, 1, 3, 1, 3]

# 列表的扩展   extend可以添加可迭代类型，可以用for遍历的都叫课迭代
list = ["hk", 67, 0, "iui"]
list1 = [0, 0, 0, 0]
list.extend(list1)
print(list)  # ['hk', 67, 0, 'iui', 0, 0, 0, 0]

list3 = [9, 9, 9, 9]
list1.extend(list3)
print(list1)  # [0, 0, 0, 0, 9, 9, 9, 9]

list4 = [7, 7, 7, 7]
new_list = list3 + list4
print(new_list)  # [9, 9, 9, 9, 7, 7, 7, 7]

str = "jkhjhkj"
list4.extend(str)
print(list4)  # [7, 7, 7, 7, 'j', 'k', 'h', 'j', 'h', 'k', 'j']
