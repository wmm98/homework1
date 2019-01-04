a = 10


def sum(a):
    a += a
    print(a)


sum(a)
print(a)
# 输出的结果分别为20和10,说明了不可变量不可改
# 数字，元组，字符串不可改


b = [11, 22]


def list(b):
     b += b
     print(b)
list(b)
print(b)
#两个print输出为相同的内容，说明元素可改