"""Zombie class"""

import enemy

zombie_path_name = "Images/Enemies/zombie_enemy.png"
SPAWN_RATE = 100

class Zombie(enemy.Enemy):

    HEALTH = 500

    def __init__(self, positionX, positionY):
        enemy.Enemy.__init__(self, positionX, positionY, Zombie.HEALTH, -2, 0, zombie_path_name)