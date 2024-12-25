"""Огнена атака"""

import basic_attack
from animations import Fire_animation
fire_attack_path = "Images/Effects/fire_attack.png"

class Fire_attack(basic_attack.Basic_attack):

    ATTACK_DAMAGE = 58

    def __init__(self, positionX, positionY, level):
        basic_attack.Basic_attack.__init__(self, positionX, positionY, level, self.ATTACK_DAMAGE, fire_attack_path, Fire_animation)