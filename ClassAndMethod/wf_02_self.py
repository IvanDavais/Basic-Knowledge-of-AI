class Cat:


    def eat_fish(self):
        print("%s love fish!" %self.name)

    def drink_water(self):
        print("%s like to drink water." %self.name)

tom = Cat()
tom.name = "Tom"
tom.drink_water()
tom.eat_fish()
# print(tom)

# addr = id(tom)
# print("%d " %addr)
# print("%x " %addr)

marry = Cat()
marry.name = "Marry"
marry.drink_water()
marry.eat_fish()
# print(marry)
# print(tom)