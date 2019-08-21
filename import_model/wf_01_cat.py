class Cat(object):
    num = 2
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Hello everyone, I am the %s cat" %self.name

    @classmethod
    def cat_num(cls):
        print("The total num of cat is %d " %cls.num)

    def hello(self):
        print("hello cat")