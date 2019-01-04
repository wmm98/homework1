# 计算某个数的阶乘时可用循环，也可用递归

# 计算4阶乘
'''
i = 1
result = 1
while i <= 4:
    result *= i
    i += 1
print(result)
'''


# 也可以用递归的方法，切记用递归方法的时候一定要控制好执行的次数
# 要不会死循环，程序奔溃



def get_nums(num):
    if num > 1:
        # return num*get_nums(num - 1)
        result = num * get_nums(num - 1)
        return result

    else:
        return num


result = get_nums(4)
print(result)
