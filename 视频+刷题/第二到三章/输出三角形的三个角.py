"""
输入三角形的三条边长度，输出三个角的角度。

如果输入的三条边长度不合法，则提示输出"Not Valid"（不含双引号，注意大小写）。

余弦定律规定，若三角形三条边(a, b, c)，边a和边b之间的夹角C满足：c2=a2+b2-2*a*b*cos(C)。

因此，

       cos(C)=(c2-a2-b2) / (-2*a*b)

       C = arccos( (c2-a2-b2) / (-2*a*b) )

在Python语言中，函数acos的作用是根据cos值求出弧度。

又，角度=弧度除以pi;再乘以180。  角度 = 弧度/pi * 180


【输入形式】

三条边a, b, c的边长（浮点数）。在一行中输入，用空格隔开。

【输出形式】

如果输入的三条边长度不合法，则提示输出"Not Valid"（不含双引号，注意大小写）。

否则，输出三个角的角度，保留两位小数。输出格式：

a: <a边的对角的角度>

b: <b边的对角的角度>

c: <c边的对角的角度>

【样例输入】

3.0 4 5
【样例输出】

a:36.87

b:53.13

c:90.00

【样例说明】
输出的是角度，不是弧度。

"""
import math

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
C = math.acos((c ** 2 - a ** 2 - b ** 2) / (-2 * a * b))
B = math.acos((b ** 2 - a ** 2 - c ** 2) / (-2 * a * c))
A = math.acos((a ** 2 - b ** 2 - c ** 2) / (-2 * b * c))


ra = A / math.pi * 180
rb = B / math.pi * 180
rc = C / math.pi * 180

'''
if a + b > c and a + c > b and b + c > a:
    print("a:"'%.2f' % ((math.acos((a ** 2 - c ** 2 - b ** 2) / (-2 * b * c))) / math.pi * 180))
    print("b:"'%.2f' % ((math.acos((b ** 2 - a ** 2 - c ** 2) / (-2 * a * c))) / math.pi * 180))
    print("c:"'%.2f' % ((math.acos((c ** 2 - b ** 2 - a ** 2) / (-2 * b * c))) / math.pi * 180))
else:
    print("Not Valid")
'''

if a + b > c and a + c > b and b + c > a:
    print("a:%.2f" % ra)
    print("b:%.2f" % rb)
    print("c:%.2f" % rc)
else:
    print("Not Valid")
