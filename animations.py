"""Всички възможни анимации, например при удар, реакция и т.н"""

import main_screen

water_animation_path = "Images/Effects/waterdrop.png"
fire_animation_path = "Images/Effects/flame.png"
light_animation_path = "Images/Effects/lightning.png"
dark_animation_path = "Images/Effects/venom.png"
vaporise_animation_path = "Images/Effects/vaporise.png"
void_animation_path = "Images/Effects/void.png"
snow_animation_path = "Images/Effects/snow_animation.png"
blood_animation_path = "Images/Effects/blood_animation.png"
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
        self.travelled_distance = 0 # при създаване на анимация е 0, защото тя ще се движи общо 20 пиксела нагоре, преди да умре

    def update(self):
        self.rect.move_ip(0, -1) # издига се нагоре
        self.travelled_distance += 1 
        if self.travelled_distance == MAX_TRAVELLED_DISTANCE: # при достигане на 20-те пиксела умира
            self.kill()

# подобно на останалите класове, както ще видите по натам в проекта, базовия клас съдържа повечето
# класовете само го наследяват и викат конструктор с правилните параметри
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


class Vaporise_animation(Animation):

    def __init__(self, positionX, positionY):
        Animation.__init__(self, positionX, positionY, vaporise_animation_path)


class Void_animation(Animation):

    def __init__(self, positionX, positionY):
        Animation.__init__(self, positionX, positionY, void_animation_path)


class Snow_animation(Animation):

    def __init__(self, positionX, positionY):
        Animation.__init__(self, positionX, positionY, snow_animation_path)


class Blood_animation(Animation):

    def __init__(self, positionX, positionY):
        Animation.__init__(self, positionX, positionY, blood_animation_path)

