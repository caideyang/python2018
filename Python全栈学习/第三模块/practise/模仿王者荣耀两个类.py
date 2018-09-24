#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/13 7:04

class Hero():
    role = "Demaxiya"
    def __init__(self, name, life_value, attack_value):
        self.name = name
        self.life_value = life_value
        self.attack_value = attack_value

    def atack(self, obj):
        obj.life_value -= self.attack_value
        print("%s 攻击%s一次，对方掉血%s" % (self.name, obj.name, self.attack_value))
        if obj.life_value <= 0:
            print("已经将【%s】杀死" % obj.name)

h1 = Hero('关羽',200,50)
h2 = Hero("吕布",300,80)
h1.atack(h2)
h2.atack(h1)
h1.atack(h2)
h2.atack(h1)

if __name__ == "__main__":
    pass