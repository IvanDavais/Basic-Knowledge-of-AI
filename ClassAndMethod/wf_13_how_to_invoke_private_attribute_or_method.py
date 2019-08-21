"""
Notice: In python program,there are no absolutely private attributes or methods,
whcih means developer can use object._ClassName__attribute, or object_ClassName_method
to invoke relative attributes or methods.

Important: In daily develop, please don't use this method to invoke private attributes
or methods
"""
class Women:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


    def __secret(self):
        print("%s 的年龄是： %d" % (self.name, self.__age))


xiaofang = Women("小方", 18)

# object._className__attribute
print(xiaofang._Women__age)

# object_className_method
xiaofang._Women__secret()