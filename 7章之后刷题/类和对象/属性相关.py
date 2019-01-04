# 限制对象创建属性
class Person:
    __slots__ = ["age"]  # 表示只允许对象添加age只一个属性，添加其他的会出错
    pass

one = Person()
one.age = 9
print(one.age)