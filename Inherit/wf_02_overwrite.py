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

# Notice when you want to overwrite a method of the parent class,
# you just need write this method again in child class.
    def bark(self):
        print("I am a special dog! ha ha ha")

xiao_tian = XiaoTiao()

xiao_tian.bark()
