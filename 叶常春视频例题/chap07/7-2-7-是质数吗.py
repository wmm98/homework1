#例7-2-7  是质数吗

n = int(input("输入一个大于10的整数："))

for k in range(2, n):
    if n % k == 0:
        break

if k == n-1:
    print(str(n) + "是质数")
else:
    print(str(n) + "不是质数")