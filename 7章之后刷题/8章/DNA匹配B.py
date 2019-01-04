'''
编写与字符串对象的find方法功能相似的函数find(srcString, substring, start, end)，
作用是在srcString串的下标start到下标end之间的片段中寻找subString串的所有出现。如果有多处出现，
各下标位置用西文逗号','隔开。如果一次都没有出现，则输出"none"。

【输入形式】

按照somestrig,substring,start,end的顺序输入，之间由空格隔开。somestring和substring均由A/T/C/G四个字母组成。
start和end由自然数构成。

【输出形式】当匹配成功时，输出子串在DNA字符串的所有位置，以子串第一个字母在DNA字符串中匹配位置的下标（从0开始），
中间用西文逗号","隔开；当匹配失败时，输出"none"。

【样例输入】ATGGCTGATGGC TGG 0 11
【样例输出】1,8

【样例输入】ATGGCTGATGGC TTT 0 11

【样例输出】none
'''


def find_index(srcString, substring, start, end):
    str1 = srcString
    result1 = []
    while True:
        if str1.find(substring, start, end) != -1:
            result1.append(str1.find(substring, start, end))
            str1 = str1.replace(substring, " " * len(substring), 1)
        else:
            break
    if len(result1) != 0:
        if len(result1) < 2:
            print(result[0])
        else:
            for i in result1[:-1]:
                print(i, end=",")
            print(result1[-1])
    else:
        print('none')

father, son, start, end = input().split()
start = int(start)
end = int(end)
result = find_index(father, son, start, end)

