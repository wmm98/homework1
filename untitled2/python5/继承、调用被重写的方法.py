# 定义父类
class Animal:
    def eat(self):
        print("-----吃----")

    def sleep(self):
        print("----睡----")

    def drink(self):
        print("----喝-----")


class Dog(Animal):
    def bark(self):
        print("----汪汪叫----")


class YellowDog(Dog):
    def run(self):
        print("----跑-----")

    # 重写父类点的方法
    def bark(self):
        print("----喊叫----")

        # 调用父类的方法
        # Dog.bark(self)

        # 或者
        super().bark()


dog1 = YellowDog()
dog1.bark()
dog1.drink()
