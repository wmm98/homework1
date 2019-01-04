'''
【问题描述】求4*4矩阵两对角线之和。第一行全1，第二行全2，第三行全3，第四行全4

 

【输入形式】无输入

 

【输出形式】20
'''

# result = (1 + 2 + 3 + 4) * 2
# print(result)

# 赖红
from numpy import *
# 生成4x4的默认值为1的矩阵
data = mat(ones((4, 4)))
print(data)
for n in range(2, 5):
    data[n-1] = n  # 修改列表里的第一行之后的每一个元素
print(data)
# 将矩阵转成列表
temp = data.tolist()
print(temp)
sum = 0
for o in range(4):
    for s in range(4):
        if o + s == 3 or o == s:
            sum += temp[o][s]
print(int(sum))

# import numpy
# data = numpy.ones((4, 4))
# for i in range(2, 4):
#     data[i - 1] = i
# print(data)