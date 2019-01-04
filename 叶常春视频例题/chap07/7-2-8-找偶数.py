#例7-2-8  找偶数

#1. 输入一组数
ss = input("输入一组整数：").split()
nums = []
for s in ss:
    nums.append(int(s))

evens = []
#2. 找偶数
for n in nums:
    if n % 2 == 0:
        evens.append(n)

#3. 输出
print("偶数有：", evens)
