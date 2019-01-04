'''	
【问题描述】

编写程序，输入十进制小数（只考虑正数），把它转换为以字符串形式存储的二进制小数，输出该二进制小数字符串。
对于转换得到的二进制小数，小数点后最多保留10位。小数点后不足10位，则输出这些位，尾部不补0；小数点后超出10位，则直接舍弃超出部分。


【输入形式】

十进制浮点小数
【输出形式】

对应输入小数的二进制小数字符串。若整数部分或者小数部分为0，则输出0。比如输入0，则意味着输出0.0  。
【样例输入】

1.2
【样例输出】

1.0011001100
【样例说明】
输入为10进制小数，将该小数转化成二进制后输出。推荐采用字符串来处理生成的二进制数，特别要注意0的处理'''

# def transfor(number):
#     while True:
#         number = float(number)
#         array1 = []
#         array2 = []
#         integer = int(number)
#         floa = number - integer
#         while integer != 0:
#             array1.append(integer % 2)
#             integer = integer // 2
#         else:
#             array1.append(0)
#
#         array1.reverse()
#
#         # 删除前面的0
#         for i in range(len(array1)):
#             if array1[i] == 0:
#                 array1.remove(array1[i])
#                 if array1[i] == 1:
#                     break
#
#         while floa > 0.00001:
#             array2.append(int(2 * floa))
#             floa = floa * 2 - int(floa * 2)
#         else:
#             array2.append(0)
#         array1.append(".")
#
#         # 切取小数点后十位
#         if len(array2) > 10:
#             array = array1 + array2[:10]
#
#         for x in array:
#             print(x, end="")
#         break
#
# n = input()
# transfor(n)


number = input()
number = float(number)
array1 = []
array2 = []
integer = int(number)
floa = number - integer
while integer != 0:
    array1.append(integer % 2)
    integer = integer // 2
else:
    array1.append(0)
array1.reverse()
while floa > 0:  # 0.00001
    array2.append(int(2 * floa))
    floa = floa * 2 - int(floa * 2)
else:
    array2.append(0)
array1.append(".")

if len(array2) >= 10:
    array2 = array2[:10]

array = array1 + array2


if number > 1:
    for x in array[1:]:
        print(x, end="")
else:
    for x in array[:]:
        print(x, end="")


