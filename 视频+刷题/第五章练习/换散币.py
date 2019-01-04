'''
将n元（n是100的倍数）换成用10元、5元、2元的组合（其中每一面值都可取0），
一共有多少种组合？输入n，输出组合数。

【输入形式】


输入钱币总额n
【输出形式】

输出组合数
【样例输入】

100
【样例输出】
66'''

# n = int(input())
# flag = 0
# # flag_list = []
# for i in range(0, (n // 2 + 1)):
#     for j in range(0, (n // 2 + 1)):
#         for z in range(0, (n // 2 + 1)):
#             if i * 5 + j * 10 + z * 2 == n:
#                 flag += 1
#                 break
#
# print(flag)

# shumu=int(input())
#
# count = 0
# for n10 in range(shumu // 10 + 1):
#     for n5 in range(shumu // 5 + 1):
#         for n2 in range(shumu // 2 + 1):
#             if n10 * 10 + n5 * 5 + n2 * 2 == shumu:
#                 count += 1
#
# print(count)


shumu = int(input())

count = 0
for n10 in range(shumu // 10 + 1):
    for n5 in range((shumu - n10 * 10) // 5 + 1):
        if (shumu - n10 * 10 - n5 * 5) % 2 == 0:
            count += 1

print(count)


# 这个程序与上一个有问题的程序相比，有两点优化：
# 1.  减少了一重循环。为什么能减少呢？你想呀，当10块钱的张数和5块钱的张数定下来后，
# 余下来的钱数是固定的，记作remain。要么，remain是偶数，能用2块钱凑齐；要么remain是奇数，
# 不能用2块钱凑齐。能用2块钱凑齐，我们就增加1种换币组合。这里，压根儿不用去穷举2块钱的张数。
# 这样，以钱数10000为例，循环的次数不大于1000 * 2000。
# 2.   减少了穷举5块钱张数的范围。做法是，shumu - n10 * 10，也就是减去10块钱凑起来的钱数

