# 一个函数内部返回的是另外一个函数，称其为“返回函数"
# 返回函数不可直接调用
def getKey(inputString):
    def sum1(a, b, c):
        return a + b + c

    def sum2(a, b, c):
        return a - b - c

    if inputString == "+":
        return sum1
    elif inputString == "-":
        return sum2


result = getKey("+")
# print(result, type(result))  # <function getKey.<locals>.sum1 at 0x0000023362472B70> <class 'function'>
res = result(1, 2, 3)
print(res)

result = getKey("-")
res1 = result(1, 2, 3)
print(res1)
