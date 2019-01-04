def print_fuhao(func):
    def inner():
        print("-" * 40)
        func()
    return inner

def print_fuhao2(func):
    def inner():
        print("*" * 40)
        func()
    return inner


@print_fuhao2
@print_fuhao
def words():
    print("好好爱护哦啊后哈哈哦哦啊")


words()
# ****************************************
# ----------------------------------------
# 好好爱护哦啊后哈哈哦哦啊


# 装饰器的叠加