"""Феникс, специален герой, призован от супера на огнения магьосник"""

import troop
from lava_attack import Lava_attack
phoenix_path_name = "Images/Troops/phoenix.png"

class Phoenix_troop(troop.Troop):

    ATTACK_DELAY = 1

    def __init__(self, positionX, positionY):
        troop.Troop.__init__(self, positionX, positionY, self.ATTACK_DELAY, phoenix_path_name, Lava_attack)
        self.movement = 4

    def update(self, cycles_count):
        self.positionX += self.movement # първият войник, който може да се движи
        if self.positionX < 50 or self.positionX > 950: # при достигане на границите на екрана, си сменя посоката
            self.movement = -self.movement
        self.rect.move_ip(self.movement, 0)
        return super().update(cycles_count)
        
        

        


