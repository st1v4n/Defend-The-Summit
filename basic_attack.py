"""Базов клас за атаките"""

import main_screen
LEVEL_MULTIPLIER = 22 # формулата е ATTACK_DAMAGE + (LEVEL * LEVEL_MULTIPLIER)

class Basic_attack(main_screen.pygame.sprite.Sprite):

    def __init__(self, positionX, positionY, level, attack_damage, image_path, attack_animation):
        main_screen.pygame.sprite.Sprite.__init__(self)
        self.image = main_screen.pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (positionX, positionY)
        main_screen.attacks_group.add(self)
        self.positionX = positionX
        self.positionY = positionY
        self.level = level
        self.attack_damage = attack_damage
        self.attack_animation = attack_animation

    def update(self, enemy): # местенето на атаките и ако достигнат своята цел, правят damage, анимация и умират
        if enemy is None:
            self.kill()
            return None
        diff_x = self.positionX - enemy.positionX # разликата в позициите на атаката и чудовището
        diff_y = self.positionY - enemy.positionY
        x, y = 0, 0 # използват се, за да се сметне отместването. Ако и двете си останат 0, значи сме достигнали целта
        if abs(diff_x) > main_screen.TOLERANCE:
            if diff_x > 0:
                x = - (diff_x**0.5) - main_screen.ATTACK_MOVEMENT_ADDITION # местенето е с коренуване на разликата + бонус, за да не се получи така, че разликата да е много малка и да забием
            else:
                x = abs(diff_x) ** 0.5 + main_screen.ATTACK_MOVEMENT_ADDITION
        if abs(diff_y) > main_screen.TOLERANCE:
            if diff_y > 0:
                y = - (diff_y ** 0.5) - main_screen.ATTACK_MOVEMENT_ADDITION
            else:
                y = abs(diff_y) ** 0.5 + main_screen.ATTACK_MOVEMENT_ADDITION
        if x==0 and y==0:
            return self.do_damage(enemy) # при достигане на целта
        self.positionX += x # ако не сме достигнали целта, атаката само се мърда към нея
        self.positionY += y
        if self.positionX < 0: # ако излезнем от екрана (което не се случва, но все пак да го има)
            self.positionX = main_screen.TOLERANCE
        if self.positionY < 0:
            self.positionY = main_screen.TOLERANCE
        self.rect.move_ip(x, y)

    def do_damage(self, enemy):
        animation = self.attack_animation(enemy.positionX, enemy.positionY) # пуска анимация
        damage = self.attack_damage + (self.level*LEVEL_MULTIPLIER) # смята колко damage ще направи
        enemy.take_damage(type(self), damage) # и чудовището си обработва щетите
        self.kill() # накрая атаката умира, тъй като е изпълнила мисията си да удари чудовището

    def get_attack_damage(self):
        return self.attack_damage + (self.level*LEVEL_MULTIPLIER)
