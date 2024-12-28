"""Огненият магьосник, самия дявол, но пък е част от войниците"""

import troop
from fire_attack import Fire_attack
import phoenix_troop
import random


mage_path_name = "Images/Troops/mage.png"

class Mage_troop(troop.Troop):

    ATTACK_DELAY = 43

    def __init__(self, positionX, positionY):
        troop.Troop.__init__(self, positionX, positionY, self.ATTACK_DELAY, mage_path_name, Fire_attack)

    def update(self, cycles_count):
        if self.level >= troop.SUPER_ACTIVATION_LEVEL and self.super_activated == False: # супера на fire mage-a е да пуска феникс
            x = random.randint(50, 950) # феникса се пуска на случайни координати в долната част на екрана
            phoenix_troop.Phoenix_troop(x, 610) 
            self.super_activated = True
        return super().update(cycles_count)

        


