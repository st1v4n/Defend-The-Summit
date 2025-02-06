"""Чудовища"""


import main_screen
import water_attack
import fire_attack
import light_attack
import lightning_attack
import dark_attack
from animations import Vaporise_animation, Void_animation

COINS_ON_DEATH = 10
BOSS_DAMAGE_MULTIPLIER = 0.7

class Enemy(main_screen.pygame.sprite.Sprite):

    def __init__(self, positionX, positionY, health, move_x, move_y, image_path, is_boss = False):
        main_screen.pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.positionX = positionX
        self.positionY = positionY
        self.move_x = move_x
        self.move_y = move_y
        self.is_boss = is_boss # всяко чудовище по дефаулт не е бос, освен ако класът, който го наследяване, не му каже че е
        self.direction = "-x" # заради картата, по дефайлт чудовищата първо ще се движат наляво, а след това надолу ще разберете как завиват
        self.at_checkpoint = 0 # от checkpoints list-a в main_screen
        self.travelled_distance = 0 # за по лесно да разберем кое чудовище е най-отпред
        self.last_attacks = [] # заради реакциите, които могат да се случат
        self.image = main_screen.pygame.image.load(image_path) 
        self.rect = self.image.get_rect()
        self.rect.center = (self.positionX, self.positionY)
        main_screen.enemy_group.add(self)
        self.at_checkpoint = 0

    def update(self): # казахте, че искате да се движат в различна траектория, ето ви и начина, по който го постигнх
        self.display_health()
        # движението е базирано на картата, която е заложена за проекта
        # не работи за други карти
        try:
            if self.direction == "-x" and self.positionX <= main_screen.checkpoints[self.at_checkpoint]: # завива надолу
                self.move_y = -self.move_x
                self.move_x = 0
                self.direction = "y"
                self.at_checkpoint += 1
            if self.direction == "y" and self.positionY >= main_screen.checkpoints[self.at_checkpoint]: # завива надясно
                self.move_x = self.move_y
                self.move_y = 0
                self.direction = "x"
                self.at_checkpoint += 1
            if self.direction == "x" and self.positionX >= main_screen.checkpoints[self.at_checkpoint]: # завива надолу
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
                main_screen.game_started = False # просто спира да spawn-ва чудовища, няма да правя end screen
        self.rect.move_ip(self.move_x, self.move_y)
        self.positionX += self.move_x
        self.positionY += self.move_y
        self.travelled_distance += abs(self.move_x) + self.move_y

    def _trigger_vaporise(self): # Vaporise e атака, която намалява с 15% текущото здраве на чудовището
        Vaporise_animation(self.positionX, self.positionY)
        self.health *= main_screen.VAPORISE_MULTIPLIER

    def _trigger_void(self): # Void e атака, която бута чудовището назад
        Void_animation(self.positionX, self.positionY)
        push_x = -self.move_x * main_screen.VOID_PUSH_BACK
        push_y = -self.move_y * main_screen.VOID_PUSH_BACK
        self.rect.move_ip(push_x, push_y)
        self.positionX += push_x
        self.positionY += push_y
        self.travelled_distance -= abs(push_x + push_y)

    def _is_reaction_triggered(self): # проверява дали се е случила реакция
        if self.is_boss: # на босовете не могат да се случват реакции
            return None
        if self.last_attacks[0] == water_attack.Water_attack and self.last_attacks[1] == fire_attack.Fire_attack:
            return self._trigger_vaporise()
        if self.last_attacks[1] == water_attack.Water_attack and self.last_attacks[0] == fire_attack.Fire_attack:
            return self._trigger_vaporise()
        if self.last_attacks[0] == dark_attack.Dark_attack and self.last_attacks[1] == light_attack.Light_attack:
            return self._trigger_void()
        if self.last_attacks[1] == dark_attack.Dark_attack and self.last_attacks[0] == light_attack.Light_attack:
            return self._trigger_void()
        if self.last_attacks[0] == dark_attack.Dark_attack and self.last_attacks[1] == lightning_attack.Lightning_attack:
            return self._trigger_void()
        if self.last_attacks[1] == dark_attack.Dark_attack and self.last_attacks[0] == lightning_attack.Lightning_attack:
            return self._trigger_void()

    def take_damage(self, attack_type, incoming_damage): # взима damage и записва каква атака го е ударила, за да провери за реакция
        self.health -= incoming_damage
        if len(self.last_attacks) < 2:
            self.last_attacks.append(attack_type)
        else:
            self.last_attacks[0] = self.last_attacks[1]
            self.last_attacks[1] = attack_type
        if len(self.last_attacks) == 2:
            self._is_reaction_triggered()
        if self.health <= 0: # ако умре чудовище, играча получава 10 coins
            main_screen.coins += COINS_ON_DEATH
            self.kill()

    def display_health(self): # просто текст, показващ здравето на чудовището, под него
        health_to_display = main_screen.main_font.render(str(int(self.health)), True, main_screen.black_color)
        rectangle = health_to_display.get_rect()
        rectangle.center = (self.positionX, self.positionY + main_screen.TEXT_DISPLAY)
        main_screen.screen.blit(health_to_display, rectangle)

    def get_direction(self):
        return self.direction
    
    def get_health(self):
        return self.health
    
    def get_movement_speed(self):
        return (self.move_x*self.move_x + self.move_y*self.move_y)**0.5

