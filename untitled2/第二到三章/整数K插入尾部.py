a = input().split()
k = int(input())
b = []
for i in a:
    b.append(int(i))
b.append(k)
for j in b:
    print(j, end=" ")
