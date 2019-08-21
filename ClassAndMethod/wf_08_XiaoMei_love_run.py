class Human:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "My name is %s, my weight is %.2f" % (self.name, self.weight)

    def run(self):
        self.weight -= 1
        print("I love running!")

    def eat(self):
        self.weight += 2
        print("I love eating! ")


xiao_ming = Human("小明", 28.0)
xiao_ming.run()
xiao_ming.eat()
print(xiao_ming)
print("")

xiao_mei = Human("小美", 39.0)
xiao_mei.eat()
xiao_mei.run()
print(xiao_mei)