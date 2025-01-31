"""Всички налични бутони"""

import main_screen
import logics


buy_button_path = "Images/Buttons/buy_button.png"
upgrade_button_path = "Images/Buttons/upgrade_button.png"
max_upgrade_button_path = "Images/Buttons/max_upgrade_button.png"
button_press_animation_path = "Images/Buttons/button_press_animation.png"
freeze_potion_button_path = "Images/Buttons/freeze_potion.png"
damage_potion_button_path = "Images/Buttons/damage_potion.png"

class Button(main_screen.pygame.sprite.Sprite):

    def __init__(self, positionX, positionY, image_path):
        main_screen.pygame.sprite.Sprite.__init__(self)
        self.positionX = positionX
        self.positionY = positionY
        self.animation = None # при натискане около бутона се появяват зелени рамки и стрелки, индикиращи, че сме го натиснали
        self.image = main_screen.pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (self.positionX, self.positionY)
        main_screen.buttons_group.add(self)

    def validate(self, mouse_x, mouse_y): # дали натискане на мишката отговаря на бутон
        if mouse_x >= self.positionX - main_screen.BUTTON_WIDTH/2 and mouse_x <= self.positionX + main_screen.BUTTON_WIDTH/2:
            if mouse_y >= self.positionY - main_screen.BUTTON_HEIGHT/2 and mouse_y <= self.positionY + main_screen.BUTTON_HEIGHT/2:
                return True
        return False
    

class Button_Press_animation(main_screen.pygame.sprite.Sprite): # просто слага украса на бутоните, да знаем че е натиснат

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


class Freeze_potion_button(Button): # нашата freeze potion-ка, която забавя всички чудовища на екрана с 50%

    def __init__(self, positionX, positionY):
        Button.__init__(self, positionX, positionY, freeze_potion_button_path)

    def update(self, positionX, positionY):
        logics.freeze_potion_activation()


class Damage_potion_button(Button): # нашата damage potion-ка, която нанася щети на всички чудовища на екрана, равни на 30% от техния живот

    def __init__(self, positionX, positionY):
        Button.__init__(self, positionX, positionY, damage_potion_button_path)

    def update(self, positionX, positionY):
        logics.damage_potion_activation()


