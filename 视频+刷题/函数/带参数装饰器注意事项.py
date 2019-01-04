# # 当程序有返回值的时候
# def print_num(func):
#     def inner(n, m):
#         print("*" * 30)
#         func(n, m)
#
#     return inner
#
#
# @print_num
# def pnum(n, m):
#     print(n, m)
#
#
# pnum(1, 2)  # 相当于调用inner函数，所以在在这里赋值的时候，
# # 所以要传相应的参数到inner函数里面，而后面还要调用pnum函数
# # 其函数也要传相对应得函数




# 当有几个函数的的时候，不能每个函数都配有有个装饰器，这样代码就会冗余
# 可以用缺省参数的办法解决问题，即用元组和字典来接收传进来的参数

def print_num(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)  # 拆包

    return inner


@print_num
def pnum(n, m):
    print(n, m)


@print_num
def pnum1(n1, n2, n3):
    print(n1, n2, n3)


pnum(1, 2)

pnum1(3, 0, n3="000")

