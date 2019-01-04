
import random

# l = [1, 2, 3, 4, 5]
# # 打乱列表顺序
# result = random.shuffle(l)
# print(result, l)  # None [4, 5, 3, 2, 1]
# # 这个方法直接修改了原来列表的值

# l = [1, 2, 3, 4, 5]
# # 反转字符串
# result = l.reverse()
# print(result, l)  # None [5, 4, 3, 2, 1]
# # 这个方法直接修改了原来列表的值

l = [1, 2, 3, 4, 5]
# 切片
result = l[::-1]
print(result, l)  # [5, 4, 3, 2, 1] [1, 2, 3, 4, 5]
# 并没有改变原来的列表