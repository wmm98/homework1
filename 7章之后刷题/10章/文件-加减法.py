'''1.	
【问题描述】

从文件jisuan.txt读入任意多行。每一行写有一个两个操作数参加的加法运算式或减法运算式。
程序分析每一行的运算式，完成运算，把运算结果写入jieguo.txt，一行一个结果。
【输入形式】

文件內的每一行 是一个两个操作数参加的加法运算式或减法运算式。算式中不含空格
【输出形式】

文件，一行一个结果。结果保留两位小数。
【样例输入】

输入文件内容：

1+2
5-2.3
6+0.8

【样例输出】

输出文件内容：

3.00
2.70
6.80'

'''


# while True:
#     ji_suan = input()
#
#     if ji_suan == "":
#         break
#     if "+" in ji_suan:
#         ji_suan1 = ji_suan.split("+")
#         result = float(ji_suan1[0]) + float(ji_suan1[1])
#         file.writelines("%0.2f\n" % result)
#     else:
#         ji_suan1 = ji_suan.split("-")
#         result = float(ji_suan1[0]) - float(ji_suan1[1])
#         file.writelines("%0.2f\n" % result)

# for line in file.readlines():  # 依次读取每行
#     line = line.strip()  # 去掉每行头尾空白
#     print(line)

file = open("jisuan.txt", "r")
file1 = open("jieguo.txt", "w+")
for line in file.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    if "+" in line:
        ji_suan1 = line.split("+")
        result = float(ji_suan1[0]) + float(ji_suan1[1])
        file1.write("%0.2f\n" % result)
    else:
        ji_suan1 = line.split("-")
        result = float(ji_suan1[0]) - float(ji_suan1[1])
        file1.write("%0.2f\n" % result)
# for line in file1.readlines():
#     print(line)
file.close()