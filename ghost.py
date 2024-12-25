"""Дух"""

import enemy

ghost_path_name = "Images/Enemies/ghost_enemy.png"
SPAWN_RATE = 50

class Ghost(enemy.Enemy):

    HEALTH = 240

    def __init__(self, positionX, positionY):
        enemy.Enemy.__init__(self, positionX, positionY, Ghost.HEALTH, -4, 0, ghost_path_name)