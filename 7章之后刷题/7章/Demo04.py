# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:15:02 2018

@author: hp
"""
'''
10 80000 2 6000 7 300 5 10 18 0
3 6000 5 20 8 10 6 0
'''

resultList = []
resultDict = {}
numberDict1 = {}
line1 = [int(n) for n in input().split()]

for i in range(0, len(line1)):
    if i == 0:
        numberDict1.update({line1[i]: line1[i + 1]})
    if i % 2 == 0:
        numberDict1.update({line1[i]: line1[i + 1]})
# print(numberDict1)
# {10: 80000, 2: 6000, 7: 300, 5: 10, 18: 0}

numberDict2 = {}
line2 = [int(n) for n in input().split()]

for i in range(0, len(line2)):
    if i == 0:
        numberDict2.update({line2[i]: line2[i + 1]})
    elif i % 2 == 0:
        numberDict2.update({line2[i]: line2[i + 1]})
# print(numberDict2)
# {3: 6000, 5: 20, 8: 10, 6: 0}


for key1, value1 in numberDict1.items():
    for key2, value2 in numberDict2.items():
        resultList.append([key1 * key2, value1 + value2])

resultList.sort(key=lambda x: x[1], reverse=True)
# print(resultList)
#  [[30, 86000], [50, 80020], [80, 80010], [60, 80000], [6, 12000], [21, 6300], [10, 6020], [16, 6010], [15, 6010], [12, 6000],
#  [54, 6000], [35, 320], [56, 310], [42, 300], [25, 30], [40, 20], [90, 20], [30, 10], [144, 10], [108, 0]]

resultListF = [[resultList[0][0], resultList[0][1]]]
# print(resultListF)
# [[30, 86000]]



# 幂相同的时候
# 系数加起来
# 然后往新列表里传

for i in range(1, len(resultList)):
    if resultList[i][1] == resultListF[len(resultListF) - 1][1]:
        resultListF[len(resultListF) - 1][0] += resultList[i][0]
    elif resultList[i][1] != resultListF[len(resultListF) - 1][1]:
        resultListF.append([resultList[i][0], resultList[i][1]])
# print(resultListF)

# [[30, 86000], [50, 80020], [80, 80010], [60, 80000], [6, 12000], [21, 6300], [10, 6020], [31, 6010], [66, 6000], [35, 320],
# [56, 310], [42, 300], [25, 30], [130, 20], [174, 10], [108, 0]]
# print(len(resultList))
# print(len(resultListF))

for i in range(0, len(resultListF)):
    print(resultListF[i][0], end=' ')
    print(resultListF[i][1], end=' ')

