'''【问题描述】

输入一组无序的整数，编程输出其中出现次数最多的整数及其出现次数。

【输入形式】

先从标准输入读入整数的个数（大于等于1，小于等于100），然后在下一行输入这些整数，各整数之间以一个空格分隔。

【输出形式】

在标准输出上输出出现次数最多的整数及其出现次数，两者以一个空格分隔；若出现次数最多的整数有多个，则按照整数升序分行输出。

【样例输入】

10

0 -50 0 632 5813 -50 9 -50 0 632

【样例输出】

-50 3

0 3

【样例说明】

输入了10个整数，其中出现次数最多的是-50和0，都是出现3次。'''

# n = int(input())
# dic = {}
# if 1 <= n <= 100:
#     num_list = [int(i) for i in input().split()]
#     # print(num_list)
#     for j in num_list:
#         d = {j: num_list.count(j)}
#         dic.update(d)
#
#     dic1 = {}
#     maxTime = max(dic.values())
#     print(maxTime)
#     for item in dic:
#         if dic[item] == maxTime:
#             dic1[item] = maxTime
#
#     for r in sorted(dic1.keys()):
#         print(r, dic[r])

num = int(input())
numList = input().split()
numDict = {}
maxNum = 0
for i in range(numList.__len__()):
    if numList[i] not in numDict:
        numDict[numList[i]] = numList.count(numList[i])
        if numList.count(numList[i]) > maxNum:
            maxNum = numList.count(numList[i])

result = []
for i in numDict:
    if numDict[i] == maxNum:
        result.append(int(i))
print(result)
# [0, -50]
for i in sorted(result):
    print(i, maxNum)