class Home:

    def __init__(self, new_area, new_addr):
        self.area = new_area
        self.addr = new_addr
        self.left_area = new_area
        self.contain_item = []

    def __str__(self):
        return "房子总面积是%d平米,还剩下%d平米，在%s" % (self.area, self.left_area, self.addr) +\
               "当前的房子有%s" % (str(self.contain_item))

    def add_item(self, item):
        self.left_area -= item.get_area()
        self.contain_item.append(item.get_name())


class Bed:

    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return "床的牌子是%s,有%d平米" % (self.name, self.area)

    def get_name(self):
        return self.name

    def get_area(self):
        return self.area


family = Home(120, "佛山市南海区广东东软学院")
print(family)

bed = Bed("宜家", 6)
print(bed)

bed1 = Bed("日本牌", 4)
print(bed1)

bed2 = Bed("美国牌", 5)
print(bed2)

family.add_item(bed)
print(family)

family.add_item(bed1)
print(family)

family.add_item(bed2)
print(family)