# 例4-1-4  遍历矩阵

# mtx是4X4矩阵
mtx = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
# 求每一行的和
row_sum = []
for r in range(4):  # range(4)等同于range(0, 4)
    sum = 0
    for c in range(4):
        sum += mtx[r][c]
    row_sum.append(sum)
print("各行的和：", row_sum)

# 求两条对角线的和
djx_sum = 0
for r in range(4):
    djx_sum += mtx[r][r]  # 左上右下对角线的元素，行号等于列号
for r in range(4):
    djx_sum += mtx[r][3 - r]  # 左下右上对角线元素，列号 = 3 - 行号 （行号列号从0开始）
print("两条对角线之和：", djx_sum)
