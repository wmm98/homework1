# 例9-3-2  重写父类方法
# 鸭子父类
class Yazi:
    def __init__(self, type, height):
        self.type = type
        self.height = height

    def jiaosheng(self):
        print("嘎嘎")


# 橡皮鸭
class Xiangpiya(Yazi):
    def __init__(self, type, height):
        super().__init__(type, height)

    # 重写了Yazi父类的jiaosheng方法
    def jiaosheng(self):
        print("唧唧")


# 水鸭
class Shuiya(Yazi):
    # 继承了Yazi父类的jiaosheng方法
    def __init__(self, type, height):
        super().__init__(type, height)


# 野鸭
class Yeya(Yazi):
    def __init__(self, type, height):
        super().__init__(type, height)

    # 重写了Yazi父类的jiaosheng方法
    def jiaosheng(self):
        print("咕咕")


xpy = Xiangpiya("橡皮鸭", 3)
print("橡皮鸭的叫声:")
xpy.jiaosheng()
sy = Shuiya("水鸭", 0.5)
print("水鸭的叫声:")
sy.jiaosheng()
yy = Yeya("野鸭", 0.6)
print("野鸭的叫声:")
yy.jiaosheng()
