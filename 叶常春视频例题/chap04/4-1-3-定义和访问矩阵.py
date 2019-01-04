# 例4-1-3  定义和访问矩阵

# 定义2行3列的整数矩阵
imx = [
    [1, 2, 3],
    [4, 5, 6]
]

# 用下标访问矩阵元素
print("整数矩阵中第1行第2列的元素：", imx[0][1])
print("整数矩阵中第2行第3列的元素：", imx[1][2])
print("整数矩阵中第1行：", imx[0])  # 可见，矩阵是列表为元素的列表
print("整数矩阵中第2行：", imx[1])

# 定义5行5列的字符矩阵
cmx = [
    "1abcd",  # 实质上，一个字符串就是一个列表
    "2efgh",
    "3ijkl",
    "4mnop",
    "5qrst"
]

# 用下标访问矩阵元素
print("字符矩阵中第2行第2列的元素：", cmx[1][1])
print("字符矩阵中第5行第3列的元素：", cmx[4][2])
print("字符矩阵中第2行：", cmx[1])
print("字符矩阵中第5行：", cmx[4])
