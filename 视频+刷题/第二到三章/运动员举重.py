"""
【问题描述】

从键盘输入两个举重运动员的成绩信息：
   姓名、体重、抓举成绩、挺举成绩
输出获胜运动员的姓名。


总成绩高者获胜（总成绩=抓举成绩+挺举成绩）
总成绩相同时，体重轻者获胜。
【输入形式】姓名1 体重1 抓举成绩1 挺举成绩1  姓名2 体重2 抓举成绩2 挺举成绩2 
【输出形式】获胜运动员的姓名
【样例输入】athlete1  78 120 130  athlete2 80 121 128
【样例输出】athlete1

"""
str1 = input().split()
total1 = eval(str1[2]) + eval(str1[3])
total2 = eval(str1[6]) + eval(str1[7])
if total1 > total2:
    print(str1[0])
elif total1 == total2:
    if eval(str1[1]) < eval(str1[5]):
        print(str1[0])
    else:
        print(str1[4])
else:
    print(str1[4])
