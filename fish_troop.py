"""Рибата, войник"""
import troop
from water_attack import Water_attack

fish_path_name = "Images/Troops/fish_troop.png"

class Fish_troop(troop.Troop):

    ATTACK_DELAY = 89

    def __init__(self, positionX, positionY):
        troop.Troop.__init__(self, positionX, positionY, self.ATTACK_DELAY, fish_path_name, Water_attack)

    def update(self, cycles_count):
        if self.level >= troop.SUPER_ACTIVATION_LEVEL and self.super_activated == False:
            for ally_troop in troop.main_screen.troops_group.sprites():
                ally_troop.level += 5 # super-a на рибата е просто да вдига нивото но всички останали войници с 5
                self.super_activated = True
        return super().update(cycles_count)

        


