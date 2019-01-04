"""
【问题描述】编写一个程序，输入N个用户的姓名和电话号码，按照用户姓名的词典顺序排列输出用户的姓名和电话号码。
【输入形式】用户首先在第一行输入一个正整数，该正整数表示待排序的用户数目，然后在下面多行输入多个用户的信息，
每行的输入格式为：姓名 电话。以回车结束每个用户的输入。
【输出形式】程序输出排序后的结果。每行的输出结果格式也是： 姓名 电话。姓名和电话字段中间没有空格，要求用户
姓名不能超过10个字符，超出10个字符时候只取前10个字符作为姓名。电话号码不能超过10位，超过10位时只按10位处理。
输出姓名、电话字段各占12个字符宽，输出格式采用默认对齐方式。另外，用户的数量要求不超过50个。
【样例输入】
3
amethystic 1234567
amethyst 654321
wangwei 7645434
【样例输出】
####amethyst######654321
##amethystic#####1234567
#####wangwei#####764543
【样例说明】程序根据用户姓名的词典顺序排序，最后按照姓名#电话的格式输出。另外，由于规定姓名和电话之间用空格分割，
所以输入姓名时请将姓和名一起输入，中间不要有空格。另外输出时候程序将自动补齐12字符宽。程序输出结尾有个回车符。
上述样例输出中，#实际上是代表空格。
"""

# # # 输入的人数
# N = int(input())
# dic = {}
# if N < 50:
#     for i in range(N):
#         name, number = input().split()
#         # d = {"name": name, "number1": number}
#         # dic.update(d)
#         if len(name) >= 10 and len(number) >= 10:
#             d = {name[:10]: number[:10]}
#             # dic.update(d)
#         elif len(name) >= 10 and len(number) <= 10:
#             d = {name[:10]: number}
#             # dic.update(d)
#         elif len(name) <= 10 and len(number) >= 10:
#             d = {name: number[:10]}
#         else:
#             # len(number) > 10 and len(number) > 10
#             d = {name: number}
#         dic.update(d)
# # print(dic)
#
# for i in sorted(dic.values()):
#     # print(i.rjust(12, "#") + dic[i].rjust(12, "#"))
#     print(i.rjust(12) + dic[i].rjust(12))

# # 这种方法也可以
# for a, b in sorted(dic.items()):
#     # print(i.rjust(12, "#") + dic[i].rjust(12, "#"))
#     print(a.rjust(12) + b.rjust(12))


num = int(input())
temp = []
result = []
for n in range(num):
    temp.append(input())
temp.sort()  # 按照姓名排序
# print(temp)
# ['amethyst 654321', 'amethystic 1234567', 'wangwei 7645434']

info = []
for m in range(num):
    temp1 = temp[m]

    print(temp1)  # 一个一个地取出来切割
    # amethyst 654321
    # amethystic 1234567
    # wangwei  7645434



    info = temp1.split(" ")  # ['amethyst', '654321']每次更新一下
#     # info.append(temp1.split(" ")) #这样插入的是每一个列表
#     print(info)
#
#     # print(temp)
#     # ['amethyst 654321', 'amethystic 1234567', 'wangwei 7645434']
#     # ['amethyst 654321', 'amethystic 1234567', 'wangwei 7645434']
#     # ['amethyst 654321', 'amethystic 1234567', 'wangwei 7645434']
#

    if len(info[0]) >= 10 or len(info[1]) >= 10:
        info[0] = info[0][0: 10]
        info[1] = info[1][0: 10]


        # print(info[0].rjust(12, " ")+info[1].rjust(12, " "))
