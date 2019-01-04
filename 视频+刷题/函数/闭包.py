# 内层函数运用外层函数的的参数或变量，外层函数返回内层函数
def print_f(b):
    a = 10
    def print_ab():
        print("1")
        print(b)
    return print_ab

result = print_f(1)
# print(result)
result()
# 10
# 1
