# 现在要完成一个可以发图片和发说说的功能，按1就是发说说，其他的是发图片，而且在执行这两个功能之前要进行登录验证
# （相当于在原来的功能上在加另外一个功能）


# 首先在一般情况下，写好的代码是不能变的，不仅是业务逻辑代码还是函数体内部都不能变，
# 可以通过创建其他的函数去执行增加的功能，这时候就可以用到闭包函数

# 进行登录验证功能
def check_login(func):
    print("*******")
    def inner():
        print("登录验证...")
        func()
    return inner

# @check_login
# fss = check_login(fss)
# 上面这两行代码是等同作用的，只是python本身有一个更好的表达方式

# @check_login就相当于check_login(func)这个函数已经执行了，
# 只是还没有调用inner()函数而已，在下面物业逻辑调用的时候就会执行

# 发说说功能
@check_login
def fss():
    print("发说说")


# 发图片功能
@check_login
def ftp():
    print("发图片")


input_index = int(input())
if input_index == 1:
    fss()
else:
    ftp()


# 一开始运行还没有进行输入的时候就会出现如下结果
# *******
# *******
# 证明外层函数已经执行一遍了，说明装饰器是立马执行的