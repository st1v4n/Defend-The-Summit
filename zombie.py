"""Zombie, enemy"""

import enemy

zombie_path_name = "Images/Enemies/zombie_enemy.png"
SPAWN_RATE = 160

class Zombie(enemy.Enemy):

    HEALTH = 420

    def __init__(self, positionX, positionY):
        enemy.Enemy.__init__(self, positionX, positionY, Zombie.HEALTH, -3, 0, zombie_path_name)

    def get_spawn_rate(self):
        return SPAWN_RATE