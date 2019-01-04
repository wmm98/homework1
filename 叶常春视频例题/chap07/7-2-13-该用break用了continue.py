# 例7-2-13  是质数吗
# 本例是在例7-2-7基础上进行了改动。有意制造了错误。
n = int(input("输入一个大于10的整数："))

for k in range(2, n):
    if n % k == 0:
        continue  # 这里用continue，有什么后果？

if k == n - 1:
    print(str(n) + "是质数")
else:
    print(str(n) + "不是质数")
