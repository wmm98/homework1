# 现在有这样一个需求，就是先在666前面打印一行------或者*******等其他的符号，
# 但要是每次都要重新写一个装饰次，而且对应的函数要调用不同的装饰器要改来改去太麻烦，很笨拙

def getPrint_num(char):
    def print_num(func):
        def inner():
            print(char * 30)
            func()

        return inner

    return print_num


@getPrint_num("*")  # ()里面可以传递任意的需求
def pnum():
    print(666666)


pnum()

# ******************************
# 666666
