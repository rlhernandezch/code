#!/usr/bin/python


import random


class Enemy:
    hp = 200
    def __init__(self,atkl,atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print(self.atkl)
    
    def getHp(self):
        print("Hp is ", self.hp)

enemy1 = Enemy(40,49)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(75,90)
enemy2.getAtk()
enemy2.getHp()

playerhp = 260
enemyatakl = 60
enemyatkh  = 80

'''
while playerhp > 0:
    dmg = random.randrange(enemyatakl,enemyatkh)
    playerhp = playerhp - dmg
    if playerhp <= 30:
        playerhp = 30

    print ("Enemy strikes for", dmg, " Points of damage. Current HP is", playerhp )


    if playerhp > 30:
        continue

    print ("You have low health. you have been teleported to nearest inn")
    break
'''
