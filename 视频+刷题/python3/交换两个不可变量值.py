# 交换两个变量的值

a = 2
b = 3

# 方法一：
c = 0
a = a + b
b = a - b
a = a - b

print(a, b)

# 方法二：
a, b = b, a
print(a, b)#输出的值没有交换？？


# 方法三：
c = 0
c = a
a = b
b = c
print(a,b)
