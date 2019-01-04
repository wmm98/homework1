
# # yield, 可以去阻断当前的函数执行，然后使用next()函数，或者，__next__(),都会让函数继续执行
# ，然后执行到下一个yield语句的时候，又会被暂停

# 生成器函数碰到return语句会终止程序
def gen():
    print("xxxxx")
    yield 1
    print("a")

    yield 2
    print("b")

    yield 3
    print("c")

    yield 4
    print("d")

    yield 5
    print("e")

# 只有执行生成器的时候print("xxxxx")才会被打印
test = gen()
print(next(test))
# xxxxx
# 1
print(next(test))
# a
# 2
print(next(test))
# b
# 3
print(next(test))
# c
# 4

print(next(test))
# d
# 5