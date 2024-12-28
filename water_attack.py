"""Водна атака"""

import basic_attack
from animations import Water_animation
water_attack_path = "Images/Effects/fish_attack.png"


class Water_attack(basic_attack.Basic_attack):

    ATTACK_DAMAGE = 136

    def __init__(self, positionX, positionY, level):
        basic_attack.Basic_attack.__init__(self, positionX, positionY, level, self.ATTACK_DAMAGE, water_attack_path, Water_animation)