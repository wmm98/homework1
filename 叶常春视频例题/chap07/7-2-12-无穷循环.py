#例7-2-12  无穷循环

n = int(input("输入一个大于1的整数："))

i = 2
while i < n:
    if n % i == 0:
        break;

if i == n:
    print(str(n) + "是质数")
else:
    print(str(n) + "不是质数")