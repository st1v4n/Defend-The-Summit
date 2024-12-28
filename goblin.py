"""Чудовище, което се отличава със скорост и здраве, но пък се появява рядко"""

import enemy

goblin_path_name = "Images/Enemies/goblin.png"
SPAWN_RATE = 1660

class Goblin(enemy.Enemy):

    HEALTH = 4100

    def __init__(self, positionX, positionY):
        enemy.Enemy.__init__(self, positionX, positionY, Goblin.HEALTH, -3, 0, goblin_path_name)
