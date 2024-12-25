"""Sprite-ове, показващи оставащия ни живот"""

import main_screen

life_image_path = "Images/Effects/hearth.png"

class Life(main_screen.pygame.sprite.Sprite):

    def __init__(self, positionX, positionY):
        main_screen.pygame.sprite.Sprite.__init__(self)
        self.positionX = positionX
        self.positionY = positionY
        self.image = main_screen.pygame.image.load(life_image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (self.positionX, self.positionY)
        main_screen.lifes_group.add(self)