# 实例方法，默认第一个参数要接到一个实例
# 类方法，默认第一个参数要接到一个类
# 静态方法，静静地看着前面俩装逼，第一个参数啥也不默认接收
# 划分依据是：方法的第一个参数必须要接收的数据类型
# 不管哪一种类型方法，都是储存在类当中；没有在实例当中
# 不同类型方法的调用方式不同

class Person:

    def one(self):
        print("这是实例方法", self)

    @classmethod
    def two(cls):
        print("这是类方法", cls)

    @staticmethod
    def three():
        print("这是静态方法")


p = Person()
print(p)  # <__main__.Person object at 0x000002343AC81BA8>
p.one()
p.two()
p.three()