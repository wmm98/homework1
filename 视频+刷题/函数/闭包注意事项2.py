def out():
    out1_list = []
    for i in range(1, 4):
        def out1():
            print(i)
        out1_list.append(out1)
    return out1_list
result = out()
print(result)
# [<function out.<locals>.out1 at 0x000002A61C092B70>,
# <function out.<locals>.out1 at 0x000002A61C092BF8>,
# <function out.<locals>.out1 at 0x000002A61C092C80>]
# 结果返回的是一个列表里面有三个函数

result[0]()
result[1]()
result[2]()
# 3
# 3
# 3


def out():
    out1_list = []
    for i in range(1, 4):
        def out1(i):
            def inner():
                print(i)
            return inner
        out1_list.append(out1(i))
    return out1_list
result = out()
print(result)

result[0]()
result[1]()
result[2]()

# 1
# 2
# 3
# 闭包里面的函数执行的时候，自身没有对应的值是会根据上下文来寻找
# 而在以上函数的：
# def out1(i):
#     def inner():
#         print(i)
# 每循环一次的时候，就在外函数就是def out1(i):里面保存了一个i值，然后调用def inner():函数时，就会寻找到外
# 层的i值进行打印，这样每次循环的i值不一样打印出来的i值也不一样