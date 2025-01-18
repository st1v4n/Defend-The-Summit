"""Дух, enemy"""

import enemy

ghost_path_name = "Images/Enemies/ghost_enemy.png"
SPAWN_RATE = 55 # spawn-ва се често, но пък не е много издръжлив

class Ghost(enemy.Enemy):

    HEALTH = 220

    def __init__(self, positionX, positionY):
        enemy.Enemy.__init__(self, positionX, positionY, Ghost.HEALTH, -4, 0, ghost_path_name)