'''用匿名函数实现多个功能'''

'''
def sum(a, b, function):
    result = function(a, b)
    print(result)

sum(22, 11, lambda x, y: x + y)
sum(22, 11, lambda x, y: x - y)
'''


def num(a, b, func):
    result = func(a, b)
    print(result)

func_new = input("请输入一个新的匿名函数")
func_new = eval(func_new)  # 转换
num(11, 12, func_new)

