# -*- coding: utf-8 -*-

'''5.	
【问题描述】

证明在偶数n以内，歌德巴赫猜想是成立的。歌德巴赫猜想是：任何一个充分大的偶数都可以表示为两个素数之和。
例如,4=2+2   6=3+3   8=3+5  50=3+47。


【输入形式】

输入偶数n
【输出形式】

对每一个偶数4, 6, 8, ..., n，依次输出一行。该行内容是<偶数>=<素数1>+<素数2>，要求素数1<=素数2.
【样例输入】

6
【样例输出】

4=2+2

6=3+'''

# n = int(input())
# numList = []
#
# print(numList)
#
# result = True
# x = 2
# while x in range(2, n):
#     y = 0
#     while y < len(numList):
#         s = x % numList[y]
#         if s == 0:
#             result = False
#             break
#         else:
#             result = True
#         y += 1
#     if result:
#         numList.append(x)
#     x += 1
# ouList = []
# z = 4
# while z <= n:
#     ouList.append(z)
#     z += 2
# result = []
#
# for i in range(0, len(ouList)):
#     for j in range(0, len(numList)):
#         for k in range(j, len(numList)):
#             if ouList[i] not in result:
#                 if ouList[i] == numList[j] + numList[k]:
#                     print('%s=%s+%s' % (ouList[i], numList[j], numList[k]))
#                     result.append(ouList[i])
#                     break


