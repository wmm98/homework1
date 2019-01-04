def sum_random(a, b, *args, **args1):
    print(a)
    print(b)
    print(args)
    print(args1)

A = (11, 22)
B = {"name" : "李华","age" : 12}
sum_random(11, 22, *A, **B)