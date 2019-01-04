# 例9-1-1  定义和使用类

class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self, n):
        """模拟小狗被命令时打滚n圈"""
        print(self.name.title() + " rolled over!")
        for i in range(1, n + 1):
            print("#" + str(i))  # 输出一次表示打滚一圈


my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over(3)
