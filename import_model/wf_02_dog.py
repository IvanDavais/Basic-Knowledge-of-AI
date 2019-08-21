class Dog(object):
    num = 2

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Hello everyone, I am the %s dog" % self.name

    @classmethod
    def dog_num(cls):
        print("The total num of dog is %d " % cls.num)

    def hello(self):
        print("hello dog")