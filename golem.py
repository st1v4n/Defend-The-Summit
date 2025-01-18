"""Чудовище, което не е особено бързо, но пък е много тежко за убиване"""

import enemy

golem_path_name = "Images/Enemies/golem.png"
SPAWN_RATE = 840

class Golem(enemy.Enemy):

    HEALTH = 3360

    def __init__(self, positionX, positionY):
        enemy.Enemy.__init__(self, positionX, positionY, Golem.HEALTH, -1, 0, golem_path_name)
