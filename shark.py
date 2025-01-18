"""Акулата, специален герой, призован от супера на рибата"""

import troop
from bubbles import Bubbles_attack
shark_path_name = "Images/Troops/shark.png"

class Shark_troop(troop.Troop):

    ATTACK_DELAY = 3

    def __init__(self, positionX, positionY):
        troop.Troop.__init__(self, positionX, positionY, self.ATTACK_DELAY, shark_path_name, Bubbles_attack)
        self.movement = 4

    def update(self, cycles_count):
        self.positionX += self.movement # втория войник, който се движи
        if self.positionX < 50 or self.positionX > 950: # при достигане на границите на екрана, си сменя посоката
            self.movement = -self.movement
        self.rect.move_ip(self.movement, 0)
        return super().update(cycles_count)
        
        

        


