# 例8-4-1  交换两个数

def swap(x, y):
    t = x
    x = y
    y = t


a = 1
b = 2
print("调用swap(a, b)前，a=", a, ", b=", b)
swap(a, b)
print("调用swap(a, b)后，a=", a, ", b=", b)

# def exchange(x, y):
#     return y, x
#
# a = 3
# b = 4
# print("调用exchange(a, b)前，a=", a, ", b=", b)
# a, b = exchange(a, b)
# print("调用exchange(a, b)后，a=", a, ", b=", b)
#
# a = 5
# b = 6
# print("利用元组进行交换前，a=", a, ", b=", b)
# a, b = (b, a)
# print("利用元组进行交换后，a=", a, ", b=", b)