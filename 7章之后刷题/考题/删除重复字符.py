'''【问题描述】删除字符串中的重复字符


【输入形式】输入一个字符串，全为字母字符


【输出形式】输出删除重复字符后的字符串


【样例输入】abbcbd


【样例输出】abcd


【样例说明】删除第二个和第三个b，保留第一个遇到的不同字符。

 
 	'''
# n = input()
# str1 = []
# for j in n:
#     str1.append(j)
#
# new_str = str1
#
# for i in new_str:
#
#     while True:
#         if new_str.count(i) > 1:
#             new_str = new_str[::-1]
#             r_index = new_str.index(i)
#             new_str.remove(new_str[r_index])
#         if new_str.count(i) == 1:
#             break
# for t in new_str:
#     print(t, end="")

n = input()
str1 = []
for j in n:
    str1.append(j)

new_str = str1
for i in str1:
    while True:
        if new_str.count(i) > 1:
            new_str = new_str[::-1]

            r_index = new_str.index(i)
            new_str.remove(new_str[r_index])
            new_str = new_str[::-1]
        if new_str.count(i) == 1:
            break
for t in new_str:
    print(t, end="")
