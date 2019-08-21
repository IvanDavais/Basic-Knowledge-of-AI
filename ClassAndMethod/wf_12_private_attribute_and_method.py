class Women:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

# 类内部方法是可以访问私有属性的;同样，如果在secret方法面前加上___之后，secret方法也会变成私有方法，在类外同样无法被访问
    def secret(self):
        print("%s 的年龄是： %d" % (self.name, self.__age))


xiaofang = Women("小方", 18)

# 注意：如果使用私有属性的话，在类外部是无法访问该属性，但是
# print(xiaofang.__age)
xiaofang.secret()
