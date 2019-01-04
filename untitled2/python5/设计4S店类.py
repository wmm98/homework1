class CarStore(object):

    def select_car(self):
        pass

    def order(self, car_type):
        return self.select_car(car_type)


# 奥迪店铺
class Aodi(CarStore):

    def select_car(self, car_type):
        return A_Factory().select_car_type(car_type)


# 奔驰店铺
class BenChi(CarStore):

    def select_car(self, car_type):
        return B_Factory().select_car_type(car_type)





class A_Factory(object):

    def select_car_type(self, car_type):
        if car_type == "aodi1":
            return aodi1()
        else:
            return aodi2()



class B_Factory(object):

    def select_car_type(self, car_type):
        if car_type == "benci1":
            return benchi1()
        else:
            return benchi2()



class Car(object):

    def move(self):
        print("车在移动")

    def music(self):
        print("可以连接蓝牙")

    def stop(self):
        print("可以停止")


class aodi1(Car):

    def speed(self):
        print("可以加速")


class aodi2(Car):

    def speed1(self):
        print("可以飞速")


class benchi1(Car):

    def speed2(self):
        print("可以飞飞速")


class benchi2(Car):

    def speed3(self):
        print("可以飞飞飞速")


bc = BenChi()
B = bc.order("benchi1")
B.move()



