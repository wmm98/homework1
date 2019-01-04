# 例6-3-2  zip函数
import copy
uch = ['A', 'B', 'C', 'D']
lch = ['a', 'b', 'c', 'd']

ch_dict = zip(uch, lch)
ch_copy = copy.deepcopy(ch_dict)  # 生成一个新对象，复制了ch_dict的全部属性

print(list(ch_dict))
print(dict(ch_copy))
# [('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd')]
# {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}