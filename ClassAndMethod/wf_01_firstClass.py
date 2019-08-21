class Cat:


    def eat_fish(self):
        print("The cat love fish!")

    def drink_water(self):
        print("The cat like to drink water.")

tom = Cat()
tom.drink_water()
tom.eat_fish()
print(tom)

addr = id(tom)
print("%d " %addr)
print("%x " %addr)

marry = Cat()
print(marry)
print(tom)
