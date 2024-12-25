"""Атаката на феникса"""

import basic_attack
from animations import Fire_animation
lava_attack_path = "Images/Effects/lava_attack.png"

class Lava_attack(basic_attack.Basic_attack):

    ATTACK_DAMAGE = 50

    def __init__(self, positionX, positionY, level):
        basic_attack.Basic_attack.__init__(self, positionX, positionY, level, self.ATTACK_DAMAGE, lava_attack_path, Fire_animation)