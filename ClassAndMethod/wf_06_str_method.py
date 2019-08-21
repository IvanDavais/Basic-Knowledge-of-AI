class Cat:
    def __init__(self, name):
        self.name = name
        print("%s is this cat name" %self.name)

    def __del__(self):
        print("program over!")

    def __str__(self):
        return "[%s] is a cat,and this sentence is output by str method" % self.name

tom = Cat("Ivan")
print(tom)


