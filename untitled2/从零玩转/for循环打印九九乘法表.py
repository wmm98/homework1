
for i in range(1, 10):  # 表示行数，循环10遍
    num = range(1, i + 1)  # 表示列，行数小于列数
    for j in num:  # 遍历列
        print("%d * %d = %d\t" % (j, i, (i * j)), end="")
    print("")
