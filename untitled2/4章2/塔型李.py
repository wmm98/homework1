# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 08:39:44 2018

@author: hp
"""

N = int(input())
side = 2 * N - 1
arr = [[0 for i in range(side)] for i in range(side)]
print(arr)
# [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
data = 0
for i in range(0, int(side / 2 + 1)):
    data = 0
    for j in range(0, int(side / 2 + 1)):
        if j <= i:
            data += 1
            arr[i][j] = data
        else:
            arr[i][j] = i + 1
        arr[i][side - j - 1] = arr[i][j]
        arr[side - i - 1][j] = arr[i][j]
        arr[side - i - 1][side - j - 1] = arr[i][j]
for i in range(0, side):
    for j in range(0, side):
        print(arr[i][j], end=' ')
    print()
