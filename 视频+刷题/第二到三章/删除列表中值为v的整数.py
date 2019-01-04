num = input().split()
num1 = int(input())

for i in range(len(num)):
    num[i] = int(num[i])


while num1 in num:
    for i in num:
        if i == num1:
            num.remove(num1)
            break
for j in num:
    print(j, end=" ")




