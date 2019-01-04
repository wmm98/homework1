def getKey(a, b, c, d=1):
    print(a + b + c + d)
# test(1, 2, 3)

# 使用偏爱函数固定某个参数的值
# 先导入模块
import functools
newFunc = functools.partial(getKey, c=1)
newFunc(1, 2)