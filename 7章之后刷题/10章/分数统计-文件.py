'''
从一个文本文件内读入任意多个学生的分数，求出最高分，最低分和平均分存入文件result.txt内。

【输入形式】

一个文件，文件中分数之间由换行隔开，输入的文件名为grade.txt。输入的分数都是整数。

【输出形式】

计算出grade.txt中所有分数的最高分，最低分和平均分并分3行存入result.txt的文件内。平均分保留1位小数。

【样例输入】

60

70

80

【样例输出】

80

60

70

【样例说明】

输出的70是平均分。
'''
f1 = open("grade.txt")

list1 = f1.readlines()
print(list1)
sum = 0
max_num = -1
min_num = int(list1[0].strip())

for line in list1:
    line = int(line.strip())
    sum += line
    if line > max_num:
        max_num = line
    if line < min_num:
        min_num = line
avg_num = sum / len(list1)

f2 = open("result.txt", "w+")
f2.write(str(max_num) + "\n")
f2.write(str(min_num) + "\n")
f2.write("%.1f" % avg_num)

f1.close()
f2.close()


