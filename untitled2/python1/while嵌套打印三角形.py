# 打印倒直角三角形
i = 1
while i <= 5:
    j = 5
    while j >= i:
        print("*", end="")
        j = j - 1
    print("")
    i = i + 1

# 打印正直角三角形
i = 1
while i <= 5:
    j = 1
    while j <= 1:
        print("*", end="")
        j = j + 1
    print("")
    i = i + 1

# 打印等边三角形
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j = j + 1
    print("")
    i = i + 1
