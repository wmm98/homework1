# 例9-2-1  使用类和对象

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


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.set_odometer(5000)
print("已行驶的里程：", my_new_car.read_odometer())

my_new_car.increment_odometer(1255)
print("已行驶的里程：", my_new_car.read_odometer())
