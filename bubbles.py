"""Атаката на акулата"""

import basic_attack
from animations import Water_animation
bubbles_attack_path = "Images/Effects/bubbles.png"

class Bubbles_attack(basic_attack.Basic_attack):

    ATTACK_DAMAGE = 10

    def __init__(self, positionX, positionY, level):
        basic_attack.Basic_attack.__init__(self, positionX, positionY, level, self.ATTACK_DAMAGE, bubbles_attack_path, Water_animation)