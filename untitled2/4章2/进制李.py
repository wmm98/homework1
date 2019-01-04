# -*- coding: utf-8 -*-


'''
编写一程序，从键盘输入x,y的值（十进制形式），接着将x，y转换为16位二进制，
然后把x的高8位作为z的高8位，y的高8位作为z的低8位，最后输出z的值（十进制形式）。
【输入形式】
以十进制形式输入x和y的值，以空格隔开。
【输出形式】
以十进制形式在新的一行上输出z值。
【输入样例】
840 2177
【输出样例】
776
【样例说明】
840的二进制形式为：  0000 0011 0100 1000
2177的二进制形式为： 0000 1000 1000 0001
将840的高8位作为结果的高8位，2177的高8位作为结果的低8位，
所以结果为：0000 0011 0000 1000，即十进制形式为：776

【提示】

可能的话，利用库函数来实现十进制到二进制，二进制到十进制的转换。
'''


line = [int(n) for n in input().split()]
x = line[0]
y = line[1]
xStr = "%16s" % bin(x).replace('0b', '')
print(xStr)
#      1101001000
xLine = list(xStr)
print(xLine)
# [' ', ' ', ' ', ' ', ' ', ' ', '1', '1', '0', '1', '0', '0', '1', '0', '0', '0']
for i in range(0, len(xLine)):
    if xLine[i] == ' ':
        xLine[i] = '0'
yStr = "%16s" % bin(y).replace('0b', '')
yLine = list(yStr)
for i in range(0, len(yLine)):
    if yLine[i] == ' ':
        yLine[i] = '0'

result = []
for i in range(0, 16):
    if i < 8:
        result.append(xLine[i])
    if i >= 8:
        result.append(yLine[i - 8])

resultStr = ''
for i in range(0, len(result)):
    resultStr += result[i]

print(int(resultStr, 2))



