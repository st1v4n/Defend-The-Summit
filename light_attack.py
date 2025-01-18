"""Светлинна атака"""

import basic_attack
from animations import Light_animation
light_attack_path = "Images/Effects/light_attack.png"

class Light_attack(basic_attack.Basic_attack):

    ATTACK_DAMAGE = 100

    def __init__(self, positionX, positionY, level):
        basic_attack.Basic_attack.__init__(self, positionX, positionY, level, self.ATTACK_DAMAGE, light_attack_path, Light_animation)