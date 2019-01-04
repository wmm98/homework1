str = input().split()
str1 = []
for i in str:
    str1.append(i)

str1.sort(reverse=True)  # 表示从大到小

for i in str1:
    print(i, end=" ")