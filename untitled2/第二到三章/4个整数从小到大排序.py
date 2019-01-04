num = input().split()
for i in range(len(num)):
    num[i] = int(num[i])
num.sort()
for j in num:
    print(j, end=" ")
