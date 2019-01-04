"""
【问题描述】编写程序实现在字符串s中删除子字符串c的功能。
            
            说明：不考虑去掉子字符串c后形成的新的子字符串c。
            例如：字符串s为abcabcd，子串c为bc，则调用该函数后，结果字符串s为aad。
【输入形式】输入的第一行表示字符串s，第二行表示子串c。
【输出形式】输出的一行表示处理后的结果。
【样例输入】
abcabcd
bc
【样例输出】
aad
"""

father = input().strip()
son = input().strip()

while True:

    n = father.find(son)
    if n != -1:
        father = father.replace(son, " ")

    else:
        break

print(father.replace(" ", ""))




# s = input()
# c = input()
#
# result = s
# while True:
#     num = result.find(c)
#     if num != -1:
#         result = result.replace(c, "") # 直接这样做会报错
#     else:
#         break
# print(result)

