"""Всички налични бутони"""

import main_screen
import logics


buy_button_path = "Images/Buttons/buy_button.png"
upgrade_button_path = "Images/Buttons/upgrade_button.png"
max_upgrade_button_path = "Images/Buttons/max_upgrade_button.png"
button_press_animation_path = "Images/Buttons/button_press_animation.png"

class Button(main_screen.pygame.sprite.Sprite):

    def __init__(self, positionX, positionY, image_path):
        main_screen.pygame.sprite.Sprite.__init__(self)
        self.positionX = positionX
        self.positionY = positionY
        self.animation = None
        self.image = main_screen.pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (self.positionX, self.positionY)
        main_screen.buttons_group.add(self)

    def validate(self, mouse_x, mouse_y):
        if mouse_x >= self.positionX - main_screen.BUTTON_WIDTH/2 and mouse_x <= self.positionX + main_screen.BUTTON_WIDTH/2:
            if mouse_y >= self.positionY - main_screen.BUTTON_HEIGHT/2 and mouse_y <= self.positionY + main_screen.BUTTON_HEIGHT/2:
                return True
        return False
    

class Button_Press_animation(main_screen.pygame.sprite.Sprite):

    def __init__(self, positionX, positionY):
        main_screen.pygame.sprite.Sprite.__init__(self)
        self.positionX = positionX
        self.positionY = positionY
        self.image = main_screen.pygame.image.load(button_press_animation_path)
        self.rect = self.image.get_rect()
        self.rect.center = (self.positionX, self.positionY)
        main_screen.button_pressed_group.add(self)



class Buy_button(Button):

    def __init__(self, positionX, positionY):
        Button.__init__(self, positionX, positionY, buy_button_path)

    def update(self, positionX, positionY):
        logics.buy_troop(positionX, positionY)


class Upgrade_button(Button):

    def __init__(self, positionX, positionY):
        Button.__init__(self, positionX, positionY, upgrade_button_path)

    def update(self, positionX, positionY):
        logics.upgrade(positionX, positionY)


class Max_upgrade_button(Button):

    def __init__(self, positionX, positionY):
        Button.__init__(self, positionX, positionY, max_upgrade_button_path)

    def update(self, positionX, positionY):
        logics.max_upgrade(positionX, positionY)


