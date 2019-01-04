'''
num = input().split()
print(num)

for i in range(len(num)):
    num[i] = int(num[i])

num.sort()
print(num)

'''

num = input().split()
num1 = []
for i in num:
    num1.append(int(i))
num1.sort()

for i in num1:
    print(i, end=" ")
