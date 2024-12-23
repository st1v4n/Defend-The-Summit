"""Дух"""

import main_screen
import enemy

ghost_path_name = "Images/Enemies/ghost_enemy.png"

class Ghost(enemy.Enemy):

    HEALTH = 240

    def __init__(self, positionX, positionY):
        enemy.Enemy.__init__(self, positionX, positionY, Ghost.HEALTH, -4, 0)
        self.image = main_screen.pygame.image.load(ghost_path_name)
        self.rect = self.image.get_rect()
        self.rect.center = (self.positionX, self.positionY)
        main_screen.enemy_group.add(self)
        self.at_checkpoint = 0

    def update(self):
        enemy.Enemy.update(self)