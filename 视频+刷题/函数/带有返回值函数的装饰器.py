def print_num(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        res = func(*args, **kwargs)  # 拆包
        return res
    return inner


@print_num
def pnum(n, m):
    print(n, m)
    return n + m

result = pnum(1, 2)
print(result)
# ******************************
# 1 2
# 3

# 函数内部有返回值，那么装饰器里面也要有相应的返回值


