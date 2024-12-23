"""Базовия клас за нашите герои"""
import main_screen

class Troop(main_screen.pygame.sprite.Sprite):

    def __init__(self, attack_damage, attack_delay, positionX, positionY):
        main_screen.pygame.sprite.Sprite.__init__(self)
        self.attack_damage = attack_damage
        self.attack_delay = attack_delay
        self.positionX = positionX
        self.positionY = positionY
        self.level = 1
    
