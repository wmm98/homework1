'''
【问题描述】统计一行字符的大写字母，小写字母和数字的个数。先输出大写字母个数，在输出小写字母个数，最后输出数字个数。
【输入形式】ljaij1A
【输出形式】1

          5

          1
【提示】用字符串的方法isupper, islower来判别大小写。isdigit来判断是否是数字。'''
str_list = input()
flag1 = 0
flag2 = 0
flag3 = 0

for i in str_list:
    if i.isupper():
        flag1 += 1
    if i.islower():
        flag2 += 1
    if i.isdigit():
        flag3 += 1
print(flag1)
print(flag2)
print(flag3)