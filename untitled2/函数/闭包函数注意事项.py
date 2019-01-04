# def func():
#     a = 10
#     def Func():
#         a = 999
#         print(a)
#
#     print(a)
#     Func()
#     print(a)
#     return Func
# result = func()
# print(result)
# # 10
# # 999
# # 10

# 修改局部变量

def func():
    a = 10
    def Func():
        nonlocal a
        a = 999
        print(a)

    print(a)
    Func()
    print(a)
    return Func
result = func()
print(result)
# 10
# 999
# 99

# 当函数没有被执行的时候，函数内部只是一个标示，并没有真正意义上的结果，原本是什么就是什么，
# 执行到这一行result = func()时，已经修改a为2了，当执行到 Func() 才调用函数打印出a = 2
#
