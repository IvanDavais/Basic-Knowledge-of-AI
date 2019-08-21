class Animal:
    def eat(self):
        print("eat eat eat")

    def sleep(self):
        print("sleep sleep sleep")


class Dog(Animal):
    def bark(self):
        print("wang wang wang")


class XiaoTiao(Dog):
    def fly(self):
        print("fly fly fly")


xiao_tian = XiaoTiao()
xiao_tian.eat()
xiao_tian.bark()
xiao_tian.fly()
xiao_tian.sleep()