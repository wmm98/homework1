'''补充矩形类Rect的定义。它有长度和宽度，area方法的作用是求矩形的面积。'''

class Rect:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def area(self):
        return self.x1 * self.y1


x = float(input())
y = float(input())
r1 = Rect(x, y)
print(r1.area())