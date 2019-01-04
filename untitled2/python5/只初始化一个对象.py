# 把对象都指向一个引用
class Dog(object):
    num = None
    flag = False

    def __new__(cls, name):

        if cls.num == None:
            cls.num = object.__new__(cls)
            return cls.num
        else:
            return cls.num  # 返回上一次的创建对象的引用

    def __init__(self, name):
        if Dog.flag == False:
            self.name = name
            Dog.flag = True




dog1 = Dog("旺财")
print(id(dog1))
print(dog1.name)

dog2 = Dog("小白")
print(id(dog2))
print(dog2.name)
