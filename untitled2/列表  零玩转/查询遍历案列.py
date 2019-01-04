# 一个列表中要是有重复的元素，直接用for循环时不可以完全删除干净相同的元素的，查询也是一样,
# 因为这些方法都是从中左到右执行的，只会搜索到左边的元素


# 现在要遍历一个列表的元素并且显示出其对应的索引

# 方法一：
# list = ["a", "w", "a", "o"]
# index_count = 0
# for i in list:
#     print(i, list.index(i, index_count), end=" ")
#     # a 0 w 1 a 2 o 3
#     index_count += 1



# 方法二：
list = ["a", "w", "a", "o"]
# 创建一个列表表示list元素的索引值
ind = range(len(list))
# 遍历索引表，每个索引对应一个元素
for i in ind:
    print(i, list[i], end=" ")
# 0 a 1 w 2 a 3 o
