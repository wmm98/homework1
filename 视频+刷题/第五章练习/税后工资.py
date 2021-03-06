"""2.	
【问题描述】
假设税前工资和税率如下（s代表税前工资，t代表税率）：
s<1000    t=0%
1000<=s<2000      t=10%
2000<=s<3000  t=15%
3000<=s<4000     t=20%
4000<=s             t=25%
编写一程序，要求用户输入税前工资额，然后计算税后工资额。
【输入形式】
从键盘输入税前工资s，可以是浮点数。
【输出形式】
输出税后工资额，保留小数后两位。
【输入样例】
3000
【输出样例】
2400.00
【样例说明】
税前工资为3000，所以税率为20％，扣除税后工资为2400.00"""

s = float(input())
if s < 1000:
    ts = s
elif 1000 <= s < 2000:
    ts = s - s * 0.1
elif 2000 <= s < 3000:
    ts = s - s * 0.15
elif 3000 <= s < 4000:
    ts = s - s * 0.20
else:
    ts = s - s * 0.25
print("%0.2f" % ts)