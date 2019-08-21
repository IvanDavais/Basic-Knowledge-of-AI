class Cat:
    def __init__(self,name):
        print("This is a init method")
        self.name = name
        print("%s is this cat's name!" % self.name)


tom = Cat("Ivan")
