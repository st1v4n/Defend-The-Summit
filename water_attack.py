"""Водна атака"""

import main_screen

fish_attack_path = "Images/Effects/fish_attack.png"


class Water_attack(main_screen.pygame.sprite.Sprite):

    ATTACK_DAMAGE = 30

    def __init__(self, positionX, positionY, level):
        main_screen.pygame.sprite.Sprite.__init__(self)
        self.image = main_screen.pygame.image.load(fish_attack_path)
        self.rect = self.image.get_rect()
        self.rect.center = (positionX, positionY)
        main_screen.attacks_group.add(self)
        self.positionX = positionX
        self.positionY = positionY
        self.level = level

    def update(self, enemy):
        diff_x = self.positionX - enemy.positionX
        diff_y = self.positionY - enemy.positionY
        x, y = 0,0
        if abs(diff_x) > main_screen.TOLERANCE:
            if diff_x > 0:
                x = - (diff_x**0.5) - main_screen.ATTACK_MOVEMENT_ADDITION
            else:
                x = abs(diff_x) ** 0.5 + main_screen.ATTACK_MOVEMENT_ADDITION
        if abs(diff_y) > main_screen.TOLERANCE:
            if diff_y > 0:
                y = - (diff_y ** 0.5) - main_screen.ATTACK_MOVEMENT_ADDITION
            else:
                y = abs(diff_y) ** 0.5 + main_screen.ATTACK_MOVEMENT_ADDITION
        if x==0 and y==0:
            enemy.take_damage(self)
            self.kill()
            return None
        self.positionX += x
        self.positionY += y
        if self.positionX < 0:
            self.positionX = main_screen.TOLERANCE
        if self.positionY < 0:
            self.positionY = main_screen.TOLERANCE
        self.rect.move_ip(x, y)