str = input()

upper = 0
lower = 0
digit = 0

for i in str:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1


print(upper)
print(lower)
print(digit)


