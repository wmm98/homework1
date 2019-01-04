'''【问题描述】从文件in162.txt中连续读入10个以磅为单位的重量值，将其转换为以千克为单位的值并求和，
将计算所得的和sum输出到文件out162.txt中。
            说明：一磅等于0.454千克。
【输入形式】文件输入的每一行包含10个浮点数数值，以空格分隔。
【输出形式】文件输出一个两位小数的数值sum。
【样例输入】1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
【样例输出】4.54
【样例说明】
【评分标准】'''

f = open("in162.txt")
content = f.readlines()
# print(content)
# content = [eval(i) for i in i.split()]

for i in content:
    i = i.split()
    result = [eval(j) for j in i]
    he = sum(result) * 0.454
    f1 = open("out162.txt", "w")
    f1.write("%.2f" % he)


f.close()
f1.close()

# for line in content:
#     line = [eval(i) for i in line.strip().split(" ")]
