class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "要添加%s, 占地：%.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, house_area):
        self.house_type = house_type
        self.house_area = house_area
        self.free_area = house_area
        self.furniture_list = []

    def __str__(self):
        return ("房子户型：%s\n"
                "面积:%.2f\n"
                "剩余面积:%.2f\n"
                "家具类型:%s\n"
                % (self.house_type, self.house_area,self.free_area, self.furniture_list))

    def add_furniture(self, item):
        if item.area > self.free_area:
            print("不好意思，[%s]占地面积太大，无法添加" % item.name)
            return

        self.furniture_list.append(item.name)
        self.free_area -= item.area


bed = Furniture("席梦思", 4.0)
table = Furniture("餐厅桌", 100)
sofa = Furniture("大沙发", 6.6)
print(table)
print(bed)
print(sofa)

my_house = House("两室一厅", 50)
my_house.add_furniture(bed)
my_house.add_furniture(table)
my_house.add_furniture(sofa)
print(my_house)
