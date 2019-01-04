# 例4-1-5  矩阵的输入
# 下面用3个引号括起来的文本是注释。
'''
输入一个字符串矩阵。输入示例如下：
ab  cd ef
gh  ij  kl
mn  op  qr
'''
print("请输入3X3字符串矩阵...")
smtx = []
for r in range(3):  # 输入每一行
    line = input()
    smtx.append(line.split())  # split()方法生成列表，用作矩阵的一行
print("输入的字符串矩阵：", smtx)

# 下面用3个引号括起来的文本是注释。
'''
输入一个2X3的整数矩阵。输入示例如下：
    1  2  3
    4  5  6
'''
print("请输入2X3整数矩阵...")
imtx = []
for r in range(2):  # 输入每一行
    line = input()
    ns = line.split()  # 得到当前行中的数字字符串列表
    # 把字符串列表转换为数字列表
    n_line = []
    for s in ns:
        n = int(s)
        n_line.append(n)
    imtx.append(n_line)
print("输入的整数矩阵：", imtx)

# 下面用3个引号括起来的文本是注释。
'''
输入一行数字，存储为2X3的整数矩阵。输入示例如下：
    1  2  3  4  5  6
'''
print("请输入6个数字...")
line = input()
ss = line.split()  # 字符串列表
# 转换为整数列表
ns = []
for s in ss:
    ns.append(int(s))
# 转换为整数矩阵
nmtx = []
for r in range(2):
    n_line = []
    for c in range(3):
        n_line.append(ns[r * 3 + c])
    nmtx.append(n_line)
print("一行数字转换得到的整数矩阵是：", nmtx)
