'''
【问题描述】给定一个整数N（2 <= N <= 8），生成所有的具有下列特性的特殊的N位质数，即其前任意位都是质数。
例如，7331即是这样一个4位的质数，因为7、73和733也都是质数。
【输入形式】输入一个整数N（2 <= N <= 8）。
【输出形式】输出有若干行，每行有一个整数，该整数有N位，而且其前任意位都是质数。并且：
1.要求输出所有符合题意的质数。
2.从小到大按顺序输出，且所有行上的数字不得重复。
【样例输入】2
【样例输出】
23
29
31
37
71
73
79

【样例说明】输出2位的质数，而且其前的任何一个数也是质数。
【运行时限】要求每次运行时间限制在20秒之内。超出时间则认为程序错误。
'''


# # 判断一个数是否是质数
# def zhi_shu(b):
#         for r in range(2, b):
#             if b % r != 0:
#                 return True
#             else:
#                 return False

def zhi_shu(m):
    # 素数大于1
    if m > 1:
        for r in range(2, m):
            if m % r == 0:
                return False
        else:
            return True
    # 小于等于1的不是素数
    else:
        return False


# n = int(input())
# for i in range(23, 10 ** 8):
#     result = ""
#     flag = 0
#     if len(str(i)) == n:
#         for j in str(i):
#             result += j
#             if zhi_shu(int(result)):
#                 flag += 0
#             else:
#                 flag += 1
#         if flag == 0:
#             print(int(result))


n = int(input())
i = 23
while i >= 23:
    result = ""
    flag = 0
    if len(str(i)) == n:
        for j in str(i):
            result += j
            if zhi_shu(int(result)):
                flag += 0
            else:
                flag += 1
        if flag == 0:
            print(int(result))

    i += 2
    if len(str(i)) > n:
        break

