import pandas as pd
import numpy as np

# 测试集大小
train_size = 10

csv_data = pd.read_csv("D:/The second/second/data.csv")
data = np.array(csv_data)

# 切分数据集和测试集
train_data = data[0:train_size, :]
test_data = data[train_size:, :]

# 分离四个属性
# cls = trian_data[:,0: 4]
# 分离类别那一列
cls = train_data[:, 4]

# 条件概率矩阵，以及先验概率矩阵
probability = np.zeros((2, 4, 3))
pc = np.zeros(2,)

# 生成条件概率矩阵，求得条件概率值
for i in range(0, 2):
    cs = cls[:] == i
    cl = train_data[cs]
    pc[i] = len(cls[cs]) / float(len(cls))
    print(i, pc[i])
    for j in range(0, 4):
        for k in range(0, 3):
            col = cl[:, j]
            probability[i][j][k] = float(len(col[col[:] == k])) / len(cls[cs])
            print(i, j, k, probability[i][j][k])


# 使用贝叶斯定理进行预测
def pre(rec):
    print(rec)
    res = np.zeros((2))
    for i in range(0, 2):
        res[i] = pc[i]
        for j in range(0, 4):
            res[i] *= probability[i][j][rec[j]]
        print("class %d: %f" % (i, res[i]))
    if res[0] > res[1]:
        print("predict class 0")
    else:
        print("predict class 1")
    return res


# 遍历测试数据进行预测
for i in test_data:
    pre(i)




