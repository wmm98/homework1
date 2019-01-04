'''补充代码，定义另一个学生对象，输入其成绩，求平均成绩并输出
'''

class Student():
    def __init__(self, math, eng, pro):
        self.sno = 0
        self.name = ""
        self.mathScore = math
        self.engScore = eng
        self.proScore = pro

    def average(self):
        return (self.mathScore + self.engScore + self.proScore) / 3

m1, e1, p1 = input().split()
m1 = float(m1)
e1 = float(e1)
p1 = float(p1)
s1 = Student(m1, e1, p1)
print(s1.average())