"""Zombie class"""

import main_screen
import enemy

zombie_path_name = "Images/Enemies/zombie_enemy.png"

class Zombie(enemy.Enemy):

    HEALTH = 500

    def __init__(self, positionX, positionY):
        enemy.Enemy.__init__(self, positionX, positionY, Zombie.HEALTH, -2, 0)
        self.image = main_screen.pygame.image.load(zombie_path_name)
        self.rect = self.image.get_rect()
        self.rect.center = (self.positionX, self.positionY)
        main_screen.enemy_group.add(self)
        self.at_checkpoint = 0

    def update(self):
        enemy.Enemy.update(self)