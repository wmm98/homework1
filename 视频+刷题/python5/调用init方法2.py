class Cat:
    # 属性
    # 初始化对象  会自动调用方法
    def __init__(self, new_name, new_age):
        print("哈哈哈哈哈哈哈哈")
        self.name = new_name
        self.age = new_age

    def run(self):
        print("它在跑")

    def sleep(self):
        print("它在睡觉")

    def introduce(self):
        print("%s的年龄是%d" % (self.name, self.age))


tom = Cat("汤姆", 19)
# tom.name = "汤姆"
# tom.age = 34
tom.run()
tom.sleep()
tom.introduce()

blue_cat = Cat("蓝猫", 30)
# blue_cat.name = "蓝猫"
# blue_cat.age = 20
blue_cat.run()
blue_cat.sleep()
blue_cat.introduce()
