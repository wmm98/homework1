class Cat:
    # 属性
    # 初始化对象  会自动调用方法
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age

    def __str__(self):
        return "%s的年龄是%d" % (self.name, self.age)

    def run(self):
        print("它在跑")

    def sleep(self):
        print("它在睡觉")

    def introduce(self):
        print("%s的年龄是%d" % (self.name, self.age))


tom = Cat("汤姆", 19)
blue_cat = Cat("蓝猫", 30)

print(tom)
print(blue_cat)
