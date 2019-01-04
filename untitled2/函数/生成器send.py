# 当生成器遇到return 语句的时候就会抛出异常,生成器不可以迭代两遍，要想迭代两遍的时候就再调用一次
# 用send去调用的时候要传一个空值，因为它不能传非空值

def gen():
    print("xxxxx")
    res = yield 1
    print("a")

    res2 = yield 2
    print(res2)




# 只有执行生成器的时候print("xxxxx")才会被打印
test = gen()
print(test.send(None))
print(test.send(6666))