# 把对象都指向一个引用
class Dog(object):
    num = None

    def __new__(cls):

        if cls.num == None:
            cls.num = object.__new__(cls)
            return cls.num
        else:
            return cls.num  # 返回上一次的创建对象的引用


dog1 = Dog()
print(id(dog1))
dog2 = Dog()
print(id(dog2))
