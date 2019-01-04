n = int(input())
mianzhi = [10, 5, 2, 1]
num_mianzhi = [0, 0, 0, 0]
for i in range(4):
    num_mianzhi[i] = n // mianzhi[i]
    n -= num_mianzhi[i] * mianzhi[i]

for num in num_mianzhi:
    print(num, end=' ')
