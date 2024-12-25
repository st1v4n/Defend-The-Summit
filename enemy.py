"""Чудовища"""

import main_screen

COINS_ON_DEATH = 10

class Enemy(main_screen.pygame.sprite.Sprite):

    def __init__(self, positionX, positionY, health, move_x, move_y, image_path):
        main_screen.pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.positionX = positionX
        self.positionY = positionY
        self.move_x = move_x
        self.move_y = move_y
        self.direction = "-x"
        self.at_checkpoint = 0
        self.travelled_distance = 0 # за по лесно да разберем кое чудовище е най-отпред
        self.last_attacks = []
        self.image = main_screen.pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (self.positionX, self.positionY)
        main_screen.enemy_group.add(self)
        self.at_checkpoint = 0

    def update(self):
        self.display_health()
        try:
            if self.direction == "-x" and self.positionX <= main_screen.checkpoints[self.at_checkpoint]:
                self.move_y = -self.move_x
                self.move_x = 0
                self.direction = "y"
                self.at_checkpoint += 1
            if self.direction == "y" and self.positionY >= main_screen.checkpoints[self.at_checkpoint]:
                self.move_x = self.move_y
                self.move_y = 0
                self.direction = "x"
                self.at_checkpoint += 1
            if self.direction == "x" and self.positionX >= main_screen.checkpoints[self.at_checkpoint]:
                self.move_y = self.move_x
                self.move_x = 0
                self.direction = "y"
                self.at_checkpoint += 1
        except: # Стигнали сме до замъка
            self.kill()
            for life in main_screen.lifes_group:
                life.kill()
                break
            if len(main_screen.lifes_group) == 0:
                main_screen.game_started = False
        self.rect.move_ip(self.move_x, self.move_y)
        self.positionX += self.move_x
        self.positionY += self.move_y
        self.travelled_distance += abs(self.move_x) + self.move_y

    def take_damage(self, attack_type, incoming_damage):
        self.health -= incoming_damage
        if len(self.last_attacks) < 2:
            self.last_attacks.append(attack_type)
        else:
            self.last_attacks[0] = self.last_attacks[1]
            self.last_attacks[1] = attack_type
        if self.health <= 0:
            main_screen.coins += COINS_ON_DEATH
            self.kill()

    def display_health(self):
        health_to_display = main_screen.main_font.render(str(int(self.health)), True, main_screen.black_color)
        rectangle = health_to_display.get_rect()
        rectangle.center = (self.positionX, self.positionY + main_screen.TEXT_DISPLAY)
        main_screen.screen.blit(health_to_display, rectangle)

