"""Базовия клас за нашите герои"""
import main_screen

IMAGE_WIDTH = 70
IMAGE_HEIGHT = 70
SUPER_ACTIVATION_LEVEL = 50

class Troop(main_screen.pygame.sprite.Sprite):

    def __init__(self, positionX, positionY, attack_delay, image_path, attack_type):
        main_screen.pygame.sprite.Sprite.__init__(self)
        self.positionX = positionX
        self.positionY = positionY
        self.super_activated = False
        self.level = 1 # по дефаулт започва от 1 ниво
        self.attack_delay = attack_delay # брой цикли, които трябва да изминат, за да направи атака нашия войник
        self.attack_type = attack_type # видът на атаката
        self.image = main_screen.pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (self.positionX, self.positionY)
        main_screen.troops_group.add(self)
    
    def display_level(self):
        level_to_display = main_screen.main_font.render("Level: " + str(self.level), True, main_screen.black_color)
        rectangle = level_to_display.get_rect()
        rectangle.center = (self.positionX, self.positionY + main_screen.TEXT_DISPLAY)
        main_screen.screen.blit(level_to_display, rectangle)

    def update(self, cycles_count):
        self.display_level()
        if len(main_screen.enemy_group) and cycles_count % self.attack_delay == 0: # атакува само, ако има живо чудовище
            self.attack = self.attack_type(self.positionX, self.positionY, self.level)

    def inCoordinates(self, x, y): # проверява дали натискане на мишката съответства на даден войник
        return x >= self.positionX - IMAGE_WIDTH/2 and x <= self.positionX + IMAGE_WIDTH/2 and y >= self.positionY - IMAGE_HEIGHT/2 and y <= self.positionY + IMAGE_HEIGHT/2

