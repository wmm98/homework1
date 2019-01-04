# 例4-5-1  元组
# 定义元组
num_tuple = (200, 50, 300, 400)
# 访问元组的元素

# num_tuple.append(90)
# print(num_tuple)
# 'tuple' object has no attribute 'append'

print("1. num_tuple[0]=", num_tuple[0])
print("2. num_tuple[1]=", num_tuple[1])

# 与列表的不同。元组的元素不能改变。
# num_tuple[0] = 300    #这一行会出错

# 与列表有很多相同之处
# 统计函数
print("3. len(num_tuple)=", len(num_tuple))
print("4. sum(num_tuple)=", sum(num_tuple))
print("5. max(num_tuple)=", max(num_tuple))
# 切片
print("6. num_tuple[1:]=", num_tuple[1:])
# 拼接操作
names = ('guo', 'li')
num_names = num_tuple + names
# (200, 50, 300, 400, 'guo', 'li')
print("7. num_tuple + names =", num_names)

# 引用复制
nums = num_tuple
# 遍历元组
print("8. nums:")
for num in nums:
    print(num)
# 8. nums:
# 200
# 50
# 300
# 400
