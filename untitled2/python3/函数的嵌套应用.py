def sum_add(a, b, c):
    result = a+b+c
    return result

def avg_add(a, b, c):
    result = sum_add(num1, num2, num3)
    result = result/3
    print(result)

num1 = int(input("请输入第一个数"))
num2 = int(input("请输入第二个数"))
num3 = int(input("请输入第三个数"))
sum_add(num1, num2, num3)
avg_add(num1, num2, num3)