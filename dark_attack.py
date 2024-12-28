"""Тъмна атака"""

import basic_attack
from animations import Dark_animation
dark_attack_path = "Images/Effects/dark_attack.png"

class Dark_attack(basic_attack.Basic_attack):

    ATTACK_DAMAGE = 43

    def __init__(self, positionX, positionY, level):
        basic_attack.Basic_attack.__init__(self, positionX, positionY, level, self.ATTACK_DAMAGE, dark_attack_path, Dark_animation)