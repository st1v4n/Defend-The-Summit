"""Upgrade-ната версия на light атаката, която се активира при супер-а на нашия light troop (gamer)"""

import basic_attack
from animations import Light_animation
lightning_attack_path = "Images/Effects/shuriken.png"

class Lightning_attack(basic_attack.Basic_attack):

    ATTACK_DAMAGE = 520

    def __init__(self, positionX, positionY, level):
        basic_attack.Basic_attack.__init__(self, positionX, positionY, level, self.ATTACK_DAMAGE, lightning_attack_path, Light_animation)