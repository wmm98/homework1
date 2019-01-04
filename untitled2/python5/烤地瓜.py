class SweetPotato:

    def __init__(self):
        self.cookLevel = 0
        self.cookedString = "生的"
        self.add = []

    def __str__(self):  # 所有的调用都在这个方法里面，由它控制
        return "地瓜的状态是%s,煮了%d分钟,加了%s" % (self.cookedString, self.cookLevel, str(self.add))
        # str(self.add) 无论是列表还是词典元祖什么的，str可以直接转为字符串

    def cook(self, cook_time):
        self.cookLevel += cook_time  # 要进行累加的话，只能拿属性来存储数据，要不方法运行完之后就什么都没有了，属性一直都在
        if self.cookLevel > 0 and self.cookLevel < 3:
            self.cookedString = "生的"
        elif self.cookLevel > 3 and self.cookLevel < 8:
            self.cookedString = "熟的"
        else:
            self.cookedString = "糊的"

    def add_something(self, something):  # 添加东西
        self.add.append(something)  # 用属性进行存储数据



di_gua = SweetPotato()
print(di_gua)



di_gua.cook(1)
di_gua.add_something("芥末")
print(di_gua)


di_gua.cook(1)
di_gua.add_something("酱油")
print(di_gua)


di_gua.cook(1)
di_gua.add_something("花生油")
print(di_gua)

di_gua.cook(1)
di_gua.add_something("盐")
print(di_gua)
