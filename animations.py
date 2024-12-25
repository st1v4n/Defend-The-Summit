"""Всички възможни анимации, например при удар, реакция и т.н"""

import main_screen

water_animation_path = "Images/Effects/waterdrop.png"
fire_animation_path = "Images/Effects/flame.png"
light_animation_path = "Images/Effects/lightning.png"
dark_animation_path = "Images/Effects/venom.png"
MAX_TRAVELLED_DISTANCE = 20

class Animation(main_screen.pygame.sprite.Sprite):

    def __init__(self, positionX, positionY, image_path):
        main_screen.pygame.sprite.Sprite.__init__(self)
        self.positionX = positionX
        self.positionY = positionY
        self.image = main_screen.pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (self.positionX, self.positionY)
        main_screen.animations_group.add(self)
        self.travelled_distance = 0

    def update(self):
        self.rect.move_ip(0, -1)
        self.travelled_distance += 1
        if self.travelled_distance == MAX_TRAVELLED_DISTANCE:
            self.kill()


class Water_animation(Animation):

    def __init__(self, positionX, positionY):
        Animation.__init__(self, positionX, positionY, water_animation_path)


class Fire_animation(Animation):

    def __init__(self, positionX, positionY):
        Animation.__init__(self, positionX, positionY, fire_animation_path)



class Light_animation(Animation):

    def __init__(self, positionX, positionY):
        Animation.__init__(self, positionX, positionY, light_animation_path)


class Dark_animation(Animation):

    def __init__(self, positionX, positionY):
        Animation.__init__(self, positionX, positionY, dark_animation_path)