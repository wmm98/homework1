'''【问题描述】

请编写一加密函数encrypt (info)

      该函数对字符串info的加密规律是：对字符串的每个字母以该字母后面第4个字母加以替换。
      例如，字母'A'后面第4个字母是'E'，用'E'代替'A'，因此，"China"应译为"Glmre"。

（注意大小写。W变A，X变B，以此类推）

【输入形式】 

字符串
【输出形式】

加密后的字符串
【样例输入】

China
【样例输出】

Glmre'''


# print(upper_list)
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
# 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D']
# print(lower_list)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'
# , 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd']


s = input()


def encrypt(s):

    list1 = []
    for i in range(65, 91):
        list1.append(chr(i))
    w = ['A', 'B', 'C', 'D']
    upper_list = list1 + w

    lower_list = []
    for j in upper_list:
        lower_list.append(j.lower())

    result = ""
    for r in range(len(s)):
        if s[r].isupper():
            w_index = upper_list.index(s[r])
            result += upper_list[w_index + 4]
        if s[r].islower():
            w_index = lower_list.index(s[r])
            result += lower_list[w_index + 4]
    return result

print(encrypt(s))