'''【问题描述】
编写一函数comb( a, b)，将两个两位数的正整数a、b合并形成一个整数并返回。合并的方式是：
将a的十位和个位数依次放在结果的十位和千位上， b的十位和个位数依次放在结果的个位和百位上。
例如，当a＝45，b=12。调用该函数后，返回5241。调用该函数进行验证：从键盘输入两个整数，
然后调用该函数进行合并，并输出合并后的结果。
【输入形式】
输入两个两位数的正整数，以空格隔开。

【输出形式】

输出合并后的正整数。
【输入样例】
45 12
【输出样例】
5241'''

def comb(a, b):
    a = str(a)
    b = str(b)
    result = a[1] + b[1] + a[0] + b[0]
    if int(result) > 1000:
        return result
    elif 100 <int(result) < 1000:
        return result[1:]
    else:
        return result[2:]
a, b = input().split()
result1 = comb(int(a), int(b))
print(result1)