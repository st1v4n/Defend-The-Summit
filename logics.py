"""Всички функции, управляващи логиката на изпълнение на играта"""
import main_screen
import zombie
import ghost
import random
import fish_troop
import gamer_troop
import fire_mage
import spider_troop

def spawn_enemy():
    if main_screen.zombie_spawn_count % zombie.SPAWN_RATE == 0:
        zombie.Zombie(main_screen.DEFAULT_SPAWN_X, main_screen.DEFAULT_SPAWN_Y)
    if main_screen.zombie_spawn_count % ghost.SPAWN_RATE == 0:
        ghost.Ghost(main_screen.DEFAULT_SPAWN_X, main_screen.DEFAULT_SPAWN_Y)

def get_closest_enemy():
    if len(main_screen.enemy_group) == 0:
        return None
    max_distance = -1
    closest_enemy = None
    for sprite in main_screen.enemy_group:
        if sprite.travelled_distance > max_distance:
            max_distance = sprite.travelled_distance
            closest_enemy = sprite
    return closest_enemy

def buy_troop(x, y):
    if main_screen.coins < main_screen.TROOP_COST:
        return None
    number = random.randint(1, main_screen.TROOPS_COUNT)
    main_screen.coins -= main_screen.TROOP_COST
    if number == 1:
        return fish_troop.Fish_troop(x, y)
    if number == 2:
        return fire_mage.Mage_troop(x, y)
    if number == 3:
        return gamer_troop.Gamer_troop(x, y)
    if number == 4:
        return spider_troop.Spider_troop(x, y)
    
def upgrade(positionX, positionY):
    if main_screen.coins < main_screen.TROOP_COST or len(main_screen.troops_group) == 0:
        return None
    for sprite in main_screen.troops_group:
        if sprite.inCoordinates(positionX, positionY):
            sprite.level += 1
            main_screen.coins -= main_screen.TROOP_COST
            return None

def max_upgrade(positionX, positionY):
    if main_screen.coins < main_screen.TROOP_COST or len(main_screen.troops_group) == 0:
        return None
    for sprite in main_screen.troops_group:
        if sprite.inCoordinates(positionX, positionY):
            levels_to_add = main_screen.coins // main_screen.TROOP_COST
            sprite.level += levels_to_add
            main_screen.coins -= levels_to_add * main_screen.TROOP_COST
            return None


    