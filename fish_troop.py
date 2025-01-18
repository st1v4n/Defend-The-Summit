"""Рибата, войник"""
import troop
from water_attack import Water_attack
import random
import shark

fish_path_name = "Images/Troops/fish_troop.png"

class Fish_troop(troop.Troop):

    ATTACK_DELAY = 81

    def __init__(self, positionX, positionY):
        troop.Troop.__init__(self, positionX, positionY, self.ATTACK_DELAY, fish_path_name, Water_attack)

    def update(self, cycles_count):
        if self.level >= troop.SUPER_ACTIVATION_LEVEL and self.super_activated == False:
            for ally_troop in troop.main_screen.troops_group.sprites():
                ally_troop.level += 3 # super-a на рибата е просто да вдига нивото но всички останали войници с 3 и да призовава акулата
            x = random.randint(50, 950) # акулата се пуска на случайни координати в долната част на екрана
            shark.Shark_troop(x, 590) 
            self.super_activated = True
        return super().update(cycles_count)

        


