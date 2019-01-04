class Cat:
    # 属性

    def __init__(self):
        print("哈哈哈哈哈哈哈哈")

    def run(self):
        print("它在跑")

    def sleep(self):
        print("它在睡觉")

    def introduce(self):
        print("%s的年龄是%d" % (self.name, self.age))
tom = Cat()
tom.name = "汤姆"
tom.age = 34
tom.run()
tom.sleep()
tom.introduce()

blue_cat = Cat()
blue_cat.name = "蓝猫"
blue_cat.age = 20
blue_cat.run()
blue_cat.sleep()
blue_cat.introduce()

