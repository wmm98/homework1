num = [10]


def sum(num):
    num = num + num
    print(num)

sum(num)
print(num)

'''最后输出的结果为[10,10]和[10]
在python中一个变量是一个指引，而且
a = a + a并不等价于a+ = a,前者表示
改变变量的指引，后者表示改变变量数值'''


'''
num = [10]


def sum(num):
    num = num + num
    print(num)

sum(num)
print(num)
'''
#最终输出的两个结果都为[10,10]