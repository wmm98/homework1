'''
编写一个程序实现两个一元多项式相乘。

【输入形式】

首先输入第一个多项式中系数不为0的项的系数和指数，以一个空格分隔。且该多项式中各项的系数均为0或正整数，
系数和最高幂次不会超过int类型的表示范围。对于多项式 anxn +a n-1 x n-1 + ...+ a1x1 + a0x0 的输入方法如下： 
an  n  a n-1  n-1 ...  a1  1  a0  0  
即相邻两个整数分别表示表达式中一项的系数和指数。在输入中只出现系数不为0的项。最后一项的指数后没有空格，只有一个回车换行符。
按照上述方式再输入第二个多项式。

【输出形式】

将运算结果输出到屏幕。将系数不为0的项按指数从高到低的顺序输出，每次输出其系数和指数，均以一个空格分隔，
最后一项的指数后也可以有一个空格。

【样例输入】

10 80000 2 6000 7 300 5 10 18 0
3 6000 5 20 8 10 6 0

【样例输出】

30 86000 50 80020 80 80010 60 80000 6 12000 21 6300 10 6020 31 6010 66 6000 35 320 56 310 42 
300 25 30 130 20 174 10 108 0

【样例说明】

输入的两行分别代表如下表达式： 
10x80000 + 2x6000 + 7x300 + 5x10 + 18 
3x6000 + 5x20 + 8x10 + 6 
相乘结果为： 
30x86000 + 50x80020 + 80x80010 + 60x80000 + 6x12000 + 21x6300 + 10x6020 + 
31x6010 + 66x6000 + 35x320 + 56x310 + 42x300 + 25x30 + 130x20 + 174x10 + 108
'''

num1 = [int(n) for n in input().split()]
num2 = [int(n) for n in input().split()]

ji_shu = num1[::2]
ou_shu = num1[1::2]
# print(ji_shu)
# print(ou_shu)

ji_shu1 = num2[::2]
ou_shu1 = num2[1::2]


# [10, 2, 7, 5, 18]
# [80000, 6000, 300, 10, 0]


# 该方法不可用，因为有相同的两个十，无法识别两个索引
# ji_shu = [i2 for i2 in num1 if num1.index(i2) % 2 == 0]
# ou_shu = [i3 for i3 in num1 if num1.index(i3) % 2 != 0]

# ji_shu1 = [i2 for i2 in num2 if num2.index(i2) % 2 == 0]
# ou_shu1 = [i3 for i3 in num2 if num2.index(i3) % 2 != 0]

ji = 1
ji_list = []
for i in ji_shu:
    for j in ji_shu1:
        ji = i * j
        ji_list.append(ji)
# print(ji_list)

he = 0
he_list = []
for a in ou_shu:
    for b in ou_shu1:
        he = a + b
        he_list.append(he)
# print(he_list)
# print(len(he_list))
# print(len(ji_list))

all_list = []
for s in range(len(ji_list)):
    single_list = [0, 0]
    single_list[0] = ji_list[s]
    single_list[1] = he_list[s]
    all_list.append(single_list)
# print(all_list)

def getOne(x):
    return x[1]

l = sorted(all_list, key=getOne, reverse=True)
for h in l:
    print(h[0], h[1], end=" ")





