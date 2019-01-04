'''
9.	
【问题描述】输入两个正整数a和b（0<a，b<1000000），求出其最大公约数和最小公倍数并输出。
【输入文件】从标准输入读取一行，是两个整数a和b，以空格分隔。
【输出文件】向标准输出打印以空格分隔的两个整数，分别是a、b的最大公约数和最小公倍数。
【输入样例】12 18
【输出样例】6 36
【样例说明】12和18的最大公约数是6，最小公倍数是36.
 '''

a, b = input().split()
a = int(a)
b = int(b)
if 0 < a < 1000000 and 0 < b < 1000000:
    result = []
    for n in range(1, min(a, b) + 1):
        if a % n == 0 and b % n == 0:
            result.append(n)
    print(max(result), end=" ")

    for i in range(max(a, b), a * b + 1):
        if i % a == 0 and i % b == 0:
            print(i)
            break