str = input()
print(len(str))
flag = 0

for i in str:
    if 'a' == i:
        flag += 1

print("%d" % flag)
str = str.lower()
print(str)


