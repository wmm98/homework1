# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 09:50:42 2018

@author: hp
# """
# 【输入】
#
# 第一行为整数n，表示有n个学生，n<=180。此后每行包含一个字符串和两个整数，分别表示学生的名字（名字第一个字母大写，其余小写，
# 不含空格，且长度小于20）和出生月(1<=m<= 12)日(1 <=d<=31)。名字、月、日之间用一个空格分隔
#
# 【输出】
#
# 每组生日相同的学生，输出一行，其中前两个数字表示月和日，后面跟着所有在当天出生的学生的名字，数字、名字之间都用一个空格分隔。
# 对所有的输出，要求按日期从前到后的顺序输出。 对生日相同的名字，按名字从短到长按序输出，长度相同的按字典序输出。
# 如果没有任何生日相同的学生，
# 输出：None  。
#
# 【样例输入】
#
#
# 【样例输出】
'''
6
Avril 3 2
Candy 4 5
Tim 3 2
Sufia 4 5
Lagrange 4 5
Bill 3 2
'''

#
# 3 2 Tim Bill Avril
# 4 5 Candy Sufia Lagrange
# 【样例说明】
# 样例输出中，3月2日有Tim, Bill, Avril三个人在当日出生。'''



n = int(input())

nameList = [[0 for i in range(2)] for i in range(n)]  # 关联日期与名字
dataList = [[0 for i in range(2)] for i in range(n)]  # 记录并排序日期
# [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]


# 给nameList和dataList 赋值
for i in range(0, n):
    line = input().split(' ', 1)
    nameList[i][0] = line[0]
    nameList[i][1] = line[1]
    mouth, date = line[1].split()
    dataList[i][0] = int(mouth)
    dataList[i][1] = int(date)
# print(nameList)
# [['Avril', '3 2'], ['Candy', '4 5'], ['Tim', '3 2'], ['Sufia', '4 5'], ['Lagrange', '4 5'], ['Bill', '3 2']]
# print(dataList)
# [[3, 2], [4, 5], [3, 2], [4, 5], [4, 5], [3, 2]]

# 日期按月——>日排序日期
dataList.sort(key=lambda x: (x[0], x[1]), reverse=False)
# print(dataList)
# [[3, 2], [3, 2], [3, 2], [4, 5], [4, 5], [4, 5]]


# 按名字长度排序nameList
nameList.sort(key=lambda x: (len(x[0]), x), reverse=False)  # 按名字长度和字典顺序排序
# print(nameList)
# [['Tim', '3 2'], ['Bill', '3 2'], ['Avril', '3 2'], ['Candy', '4 5'], ['Sufia', '4 5'], ['Lagrange', '4 5']]

nameDict = {}  # 记录日期出现次数
# 记录日期出现次数
for i in range(0, n):
    # 例：将日期（3,2）转为str'3 2'
    strDate = '%d %d' % (dataList[i][0], dataList[i][1])
    # 记录日期出现次数
    if strDate not in nameDict:
        nameDict.update({strDate: 1})
    elif strDate in nameDict:
        nameDict[strDate] += 1
# print(nameDict)
# {'3 2': 3, '4 5': 3}

dataListF = []  # 转格式后的日期
for key, value in nameDict.items():
    if value > 1:
        dataListF.append(key)  # 已转格式并排序完的重复日期列表
# print(dataListF)
# ['3 2', '4 5']

# 用排列好顺序的dataList索引nameDict，找出出现次数超过1的日期
for i in range(0, len(dataListF)):
    print(dataListF[i], end=' ')
    for j in range(0, len(nameList)):
        if nameList[j][1] == dataListF[i]:
            print(nameList[j][0], end=' ')
    print()

if len(dataListF) == 0:
    print('None')
