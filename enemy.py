"""Чудовища"""

import main_screen

class Enemy(main_screen.pygame.sprite.Sprite):

    def __init__(self, positionX, positionY, health, move_x, move_y):
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

    def update(self):
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
            main_screen.castle_health -= 1
            if main_screen.castle_health == 0:
                pass
        self.rect.move_ip(self.move_x, self.move_y)
        self.positionX += self.move_x
        self.positionY += self.move_y
        self.travelled_distance += abs(self.move_x) + self.move_y

    def take_damage(self, attack_type):
        incoming_damage = attack_type.ATTACK_DAMAGE + (attack_type.level*4)
        self.health -= incoming_damage
        if len(self.last_attacks) < 2:
            self.last_attacks.append(attack_type)
        else:
            self.last_attacks[0] = self.last_attacks[1]
            self.last_attacks[1] = attack_type
        if self.health <= 0:
            self.kill()

