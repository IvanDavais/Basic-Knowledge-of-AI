class Cat:
    def __init__(self, name):
        self.name = name
        print("%s is this cat name" %self.name)

    def __del__(self):
        print("program over!")


tom = Cat("Ivan")

# del tom

print("Loot at when this will execute!")