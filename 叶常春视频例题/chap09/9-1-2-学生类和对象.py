# 例9-1-2  学生类和对象

class Student:
    def __init__(self, sno, sname, sex):
        # 设置学号、姓名和性别属性的值
        self.sno = sno
        self.sname = sname
        self.sex = sex
        # 初始化语文，数学和英语成绩。建议在构造方法内初始化所有数据属性。
        self.ywScore = 0  # 语文成绩
        self.sxScore = 0  # 数学成绩
        self.yyScore = 0  # 英语成绩

    # 设置语文成绩的方法
    def setYwScore(self, score):
        self.ywScore = score

    # 设置数学成绩的方法
    def setSxScore(self, score):
        self.sxScore = score

    # 设置英语成绩的方法
    def setYyScore(self, score):
        self.yyScore = score

    # 计算总成绩的方法
    def totalScore(self):
        return self.ywScore + self.sxScore + self.yyScore

    # 求平均分的方法
    def avgScore(self):
        return self.totalScore() / 3

    # 计算几个门数
    def jigeMenshu(self):
        cnt = 0
        if self.ywScore >= 60:
            cnt += 1
        if self.sxScore >= 60:
            cnt += 1
        if self.yyScore >= 60:
            cnt += 1
        return cnt


zhang = Student('2017001', 'Zhang', 'F')
zhang.setYwScore(88.5)
zhang.setSxScore(90.0)
zhang.setYyScore(78)
print("%s\t%s\t%f" % (zhang.sno, zhang.sname, zhang.avgScore()))
# print参数的写法格式："格式控制串"%(项1, 项2, ...)
# "%s\t%s\t%f"是格式控制串。
# 第一个格式指示符%s将用zhang.sno的值代替。第二个%s将用zhang.sname的值代替。%s是指值的类型是字符串。
# 第三个格式指示符%f将用zhang.avgScore()的值代替，类型是浮点数。
# \t是跳格符的写法，作用是在输出项之间加入空白，产生分隔效果。

li = Student('2017001', 'Li', 'F')
li.setYwScore(58.5)
li.setSxScore(100.0)
li.setYyScore(62)
print("%s\t%s\t%i" % (zhang.sno, zhang.sname, zhang.jigeMenshu()))
# 上一行中，%i将用zhang.jiegeMenshu()的值代替。类型是整数。
