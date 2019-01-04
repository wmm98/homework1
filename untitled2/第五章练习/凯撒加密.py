'''
【问题描述】

        凯撒密码是古罗马凯撒大帝用来保护重要军情的加密系统。这套密码系统在现在看来很低级，
        但是在古罗马时期还是发挥了重要作用的。

        凯撒密码的根本思想是按照字母表排列顺序将明文中每个字母变换成其后第n个字母。这里，n（n=1~25）被称作秘钥。

        请编写程序，针对不同的输入字符串和移动位数，输出经过凯撒加密之后的字符串。


【输入形式】

一行。第一个输入参数是移动的位数n，中间间隔一个空格之后，第二个输入参数是待加密的原文字符串（由大写字母和非字母的字符组成）。
【输出形式】

加密后的密文字符串。注意，只加密字母。待加密的字符串中可能包含空格，比如"HELLO WORLD"。
调用input函数输入后，再调用split()会将待加密字符串也一并分割了——这是不对的。split()方法有参数指定分割多少项，
建议采用，请上网搜索说明文档。
【样例输入】

5 NUDT
【样例输出】

SZIY
【样例说明】

输入参数中第一个参数'5'表示移动位数n=5，然后将第二个输入参数中每个字母都向后移动5位，得到输出字符串。
'''

str_list = input()
key_list = []
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
# 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 20'V', 'W', 'X', 'Y', 'Z']

l = key_list[::-1]


# print(ord("A"), ord("Z"))

for i in range(65, 91):
    key_list.append(chr(i))
# print(key_list)
result = ""
for j in str_list[2:]:
    if j.isupper():
        if key_list.index(j) + int(str_list[0]) < len(key_list):
            result += key_list[(key_list.index(j) + int(str_list[0]))]
        else:
            # result += key_list[::-1][(key_list[::-1].index(j) + int(str_list[0]))]
            long = len(key_list) - key_list.index(j)
            result += key_list[int(str_list[0]) - long]
    else:
            result += j

print(result)


# print(key_list)
# print(key_list[::-1])
# ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P',
# 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']