#例5-2-6
phy = float(input("输入物理成绩："))
che = float(input("输入化学成绩："))

if phy >= 90.0 or che >= 90.0:
    print("获得集训资格")
else:
    print("没有获得集训资格")