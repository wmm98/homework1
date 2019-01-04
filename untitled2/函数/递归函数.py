# 功能： 如果不是直接知道结果的数据就进行分解
# 如果说，直接知道结果的数据，就直接返回

# 例如计算一个数的阶乘
def jiecheng(n):
    if n == 1:
        return 1

    return n * jiecheng(n - 1)
print(jiecheng(5))
# 120