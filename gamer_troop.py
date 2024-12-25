"""геймъра"""

import troop
from light_attack import Light_attack
from lightning_attack import Lightning_attack
gamer_path_name = "Images/Troops/gamer.png"
chinese_knight_path = "Images/Troops/chinese_knight.png"

class Gamer_troop(troop.Troop):

    ATTACK_DELAY = 75

    def __init__(self, positionX, positionY):
        troop.Troop.__init__(self, positionX, positionY, self.ATTACK_DELAY, gamer_path_name, Light_attack)

    def update(self, cycles_count):
        if self.level >= troop.SUPER_ACTIVATION_LEVEL and self.super_activated == False:
            self.attack_type = Lightning_attack
            self.image = troop.main_screen.pygame.image.load(chinese_knight_path)
            self.super_activated = True
        return super().update(cycles_count)
        
        

        


