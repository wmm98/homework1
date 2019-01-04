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
print(next(test))
print(next(test))
test.close()
# close方法后面还有next语句的话会出现异常

print(next(test))


print(next(test))
# d