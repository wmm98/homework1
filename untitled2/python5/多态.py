class Dog(object):
    def print_self(self):
        print("你们好")


class YellowDog(Dog):
    def print_self(self):
        print("大家好")


def introduce(temp):
    temp.print_self()


d1 = Dog()
d2 = YellowDog()

introduce(d1)
introduce(d2)


