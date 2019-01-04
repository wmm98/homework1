def num(a, b, c=3, d=2):  # 当没有赋值给c,d时，程序默认c=3,d=2
    print(a)
    print(b)
    print(c)
    print(d)


num(1, 2)
num(2, 3, d=4)  # 当修改d而不修改C时
