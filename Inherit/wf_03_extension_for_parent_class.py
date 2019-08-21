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

# Notice: when you overwrite methods of the parent class and want to add more function in child class,
# you can use super().methodName to output content of the parent class, than you can process other design.
    def bark(self):
        print("I am a special dog! ha ha ha")

        # Notice : Two method blow both are available
        super(XiaoTiao, self).bark()
        super().bark()

        #Notice: In old version(python 2.*), users can use parentclass.method(self)
        Dog.bark(self)
        print("Good dog!")
xiao_tian = XiaoTiao()

xiao_tian.bark()
