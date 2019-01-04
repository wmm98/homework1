# 例9-3-1  继承

class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make  # 牌子
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        '''读取里程数'''
        return self.odometer

    def set_odometer(self, meter):
        '''设置里程数'''
        if meter > self.odometer:
            self.odometer = meter

    def increment_odometer(self, mileage):
        '''增加里程数'''
        self.odometer += mileage


#
# ElectricCar继承了Car。
# 1. 类名ElectricCar之后括号内的Car，表示用作父类。
# 2. 子类的构造方法中，要调用父类的构造方法。写法：super().__init__(...)
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70  # 子类的属性

    def get_battery_size(self):  # 子类的方法
        return self.battery_size


my_tesla = ElectricCar('tesla', 'model s', 2016)
# 继承使得子类拥有了父类定义的属性
print(my_tesla.get_descriptive_name())
my_tesla.set_odometer(200)
my_tesla.increment_odometer(400)

print("电池容量：", my_tesla.get_battery_size())
