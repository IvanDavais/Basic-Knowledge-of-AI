class Gun:
    def __init__(self, type, bullet_num):
        self.type = type
        self.bullet_num = bullet_num
        self.now_bullet = 0

    def __str__(self):
        return "这是一个%s, 装弹量为%d" % (self.type, self.bullet_num)

    def add_bullet(self,number):
        bullet_avaible = self.bullet_num-self.now_bullet
        if number >= bullet_avaible:
            remainder_bullet = number - bullet_avaible
            print("你想加入%d弹量，实际加入%d,弹药已加满，多余%d闲置，请尽情使用！" %(number, bullet_avaible, remainder_bullet))
            self.now_bullet = self.bullet_num
        elif number <= 0:
            print("你没有加入任何弹药，请按指示加入弹药！")
        else:
            self.now_bullet += number

    def shoot(self,num):
        # if num > self.now_bullet:
        #     print("弹药耗尽，请加弹药！")
        #     return
        self.now_bullet -= num
        print("你完成了射击,并且开了%d枪" % num)


class Solider:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def __str__(self):
        return "我叫%s, 手持%s, 载弹量%d" % (self.name, self.gun.type, self.gun.bullet_num)

    def fire(self,number):
        print("您想射击%d次" % number)
        if number > self.gun.now_bullet:
            print("你完成了%d次射击" % self.gun.now_bullet)
            print("弹药耗尽，请加弹药！")
            return
        self.gun.shoot(number)
        print("我是%s, 我完成了射击%d次的任务" % (self.name, number))


ak47 = Gun("AK47", 60)
ivan = Solider("Ivan", ak47)
print(ivan)
ivan.gun.add_bullet(96)
ivan.fire(63)
