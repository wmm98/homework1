


def all_sum(a, b, c):
    print(a + b + c)


def sum(*args):
    print(args)  # (1, 2, 3)

    # 拆包
    print(*args)  # 1 2 3

    all_sum(*args)  # 6

sum(1, 2, 3)

def my_sum1(a, b):
    print(a)
    print(b)

def my_sum(**kwargs):  # **表示以字典的形式接收参数
    print(kwargs)  # {'a': 1, 'b': 2}


    # 拆包
    # print(**kwargs) 这样是会出现异常的
    # 可以通过调用其他函数来体现
    my_sum1(**kwargs)
    # my_sum1(a=1,b=2)跟my_sum1(**kwargs)起相同作用的,所以写的时候被调用的函数一定要写对
    # 1
    # 2


my_sum(a=1, b=2)


