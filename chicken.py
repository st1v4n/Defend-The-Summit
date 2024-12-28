"""Чудовище - boss, който е труден за убиване, но пък бавен и се появява рядко"""

import enemy

chicken_path_name = "Images/Enemies/chicken.png"
SPAWN_RATE = 2500

class Chicken(enemy.Enemy):

    HEALTH = 6400

    def __init__(self, positionX, positionY):
        enemy.Enemy.__init__(self, positionX, positionY, Chicken.HEALTH, -1, 0, chicken_path_name, True)

    def take_damage(self, attack_type, incoming_damage):
        incoming_damage *= enemy.BOSS_DAMAGE_MULTIPLIER # той е boss и поема по-малко damage
        return super().take_damage(attack_type, incoming_damage)
