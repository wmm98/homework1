#例7-2-10  求及格率和平均分
#功能：输入一组整数分数，去除不合法的输入，然后求及格率和平均分

#1. 输入分数
ss = input("输入整数分数，用空格隔开：").split()

#2. 统计总人数，及格人数和平均分
total = 0   #总人数
passed = 0  #及格人数
sum = 0     #累计总分
for s in ss:
    if not s.isdigit():  #isdigit()方法用于检测是否是合法的数字
        print("去掉不是数字的项：", s)
        continue        #非数字，去掉
    score = float(s)

    total += 1
    sum += score
    if score >= 60:
        passed += 1
#下一行的输出中:
#  "及格率：%.1f%%"是格式控制串。
#     1.%f是格式化串，用于输出及格率（百分比值）。f代表要用一个浮点数代入。.1f表示小数点后保留1位。
#     2.%%是最终输出为%。只有一个%的话，则视为格式化串。
#  上述格式控制串之后的%是格式控制串和代入的值之间的分割符。
#  式子（passed / total * 100)的计算结果就是代入%f的浮点数。
print("及格率：%.1f%%"% (passed / total * 100) )
print("平均分", sum / total)
