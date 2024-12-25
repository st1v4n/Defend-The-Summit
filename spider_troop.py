"""Паяк"""

import troop
from dark_attack import Dark_attack

spider_path_name = "Images/Troops/spider.png"

class Spider_troop(troop.Troop):

    ATTACK_DELAY = 27

    def __init__(self, positionX, positionY):
        troop.Troop.__init__(self, positionX, positionY, self.ATTACK_DELAY, spider_path_name, Dark_attack)

    def update(self, cycles_count):
        if self.level >= troop.SUPER_ACTIVATION_LEVEL and self.super_activated == False:
            self.attack_delay = 1 # super-a на паяка е да става с много бърза атака
            self.super_activated = True
        return super().update(cycles_count)

        


