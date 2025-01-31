"""Всички функции, управляващи логиката на изпълнение на играта"""
import main_screen
import zombie
import ghost
import random
import fish_troop
import gamer_troop
import fire_mage
import spider_troop
import golem
import goblin
import chicken
from animations import Snow_animation, Blood_animation


def spawn_enemy():
    if main_screen.enemy_spawn_count % zombie.SPAWN_RATE == 0:
        zombie.Zombie(main_screen.DEFAULT_SPAWN_X, main_screen.DEFAULT_SPAWN_Y)
    if main_screen.enemy_spawn_count % ghost.SPAWN_RATE == 0:
        ghost.Ghost(main_screen.DEFAULT_SPAWN_X, main_screen.DEFAULT_SPAWN_Y)
    if main_screen.enemy_spawn_count % golem.SPAWN_RATE == 0:
        golem.Golem(main_screen.DEFAULT_SPAWN_X, main_screen.DEFAULT_SPAWN_Y)
    if main_screen.enemy_spawn_count % goblin.SPAWN_RATE == 0:
        goblin.Goblin(main_screen.DEFAULT_SPAWN_X, main_screen.DEFAULT_SPAWN_Y)
    if main_screen.enemy_spawn_count % chicken.SPAWN_RATE == 0:
        chicken.Chicken(main_screen.DEFAULT_SPAWN_X, main_screen.DEFAULT_SPAWN_Y)

def get_closest_enemy(): # проверява в групата с чудовища кое е най-отпред, т.е кое има най-много travelled_distance
    if len(main_screen.enemy_group) == 0:
        return None
    max_distance = -1
    closest_enemy = None
    for sprite in main_screen.enemy_group:
        if sprite.travelled_distance > max_distance:
            max_distance = sprite.travelled_distance
            closest_enemy = sprite
    return closest_enemy

def buy_troop(x, y): # логика за закупуване на войници, използвана от buy button-a 
    if main_screen.coins < main_screen.troop_buy_cost:
        return None
    number = random.randint(1, main_screen.TROOPS_COUNT) # на случаен принцип се избира кой войник ще ти даде
    main_screen.coins -= main_screen.troop_buy_cost
    main_screen.troop_buy_cost += 20 # всеки път, когато се купи нов герой, се увеличава цената на следващо закупуване
    if number == 1:
        return fish_troop.Fish_troop(x, y)
    if number == 2:
        return fire_mage.Mage_troop(x, y)
    if number == 3:
        return gamer_troop.Gamer_troop(x, y)
    if number == 4:
        return spider_troop.Spider_troop(x, y)
    
def upgrade(positionX, positionY): # upgrade-ване с 1 ниво, използвана от съответния бутон
    if main_screen.coins < main_screen.TROOP_UPGRADE_COST or len(main_screen.troops_group) == 0:
        return None
    for sprite in main_screen.troops_group:
        if sprite.inCoordinates(positionX, positionY):
            sprite.level += 1
            main_screen.coins -= main_screen.TROOP_UPGRADE_COST
            return None

def max_upgrade(positionX, positionY): # upgrade-ване с максималното количество нива, които позволяват нашите coins
    if main_screen.coins < main_screen.TROOP_UPGRADE_COST or len(main_screen.troops_group) == 0:
        return None
    for sprite in main_screen.troops_group:
        if sprite.inCoordinates(positionX, positionY):
            levels_to_add = main_screen.coins // main_screen.TROOP_UPGRADE_COST
            sprite.level += levels_to_add
            main_screen.coins -= levels_to_add * main_screen.TROOP_UPGRADE_COST
            return None
        
def display_coin_situation(): # просто текст да се знае цената на всичко, както и нашия coin balance
    coins_to_display = main_screen.main_font.render("Coins: " + str(main_screen.coins), True, main_screen.black_color)
    rectangle_coins = coins_to_display.get_rect()
    rectangle_coins.center = (1100, 200)
    main_screen.screen.blit(coins_to_display, rectangle_coins)
    buy_cost = main_screen.main_font.render("Buy cost: " + str(main_screen.troop_buy_cost), True, main_screen.black_color)
    rectangle_cost = buy_cost.get_rect()
    rectangle_cost.center = (1100, 240)
    main_screen.screen.blit(buy_cost, rectangle_cost)
    upgrade_cost = main_screen.main_font.render("Upgrade cost: " + str(main_screen.TROOP_UPGRADE_COST), True, main_screen.black_color)
    rectangle_upgrade = upgrade_cost.get_rect()
    rectangle_upgrade.center = (1100, 280)
    main_screen.screen.blit(upgrade_cost, rectangle_upgrade)

def boost_enemies(): # на всеки 5000 цикъла, чудовищата стават по-силни
    zombie.Zombie.HEALTH *= main_screen.ENEMY_BOOST_MULTIPLIER
    ghost.Ghost.HEALTH *= main_screen.ENEMY_BOOST_MULTIPLIER
    golem.Golem.HEALTH *= main_screen.ENEMY_BOOST_MULTIPLIER
    goblin.Goblin.HEALTH *= main_screen.BOSS_BOOST_MULTIPLIER
    chicken.Chicken.HEALTH *= main_screen.BOSS_BOOST_MULTIPLIER
    zombie.SPAWN_RATE -= main_screen.SPAWN_RATE_DECREASE
    ghost.SPAWN_RATE -= main_screen.SPAWN_RATE_DECREASE
    golem.SPAWN_RATE -= main_screen.SPAWN_RATE_DECREASE
    if zombie.SPAWN_RATE < main_screen.SPAWN_RATE_DECREASE:
        zombie.SPAWN_RATE = main_screen.SPAWN_RATE_DECREASE
    if ghost.SPAWN_RATE < main_screen.SPAWN_RATE_DECREASE:
        ghost.SPAWN_RATE = main_screen.SPAWN_RATE_DECREASE
    if golem.SPAWN_RATE < main_screen.SPAWN_RATE_DECREASE:
        golem.SPAWN_RATE = main_screen.SPAWN_RATE_DECREASE
    if zombie.Zombie.HEALTH >= main_screen.MAX_NUMBER:
        zombie.Zombie.HEALTH = main_screen.MAX_NUMBER / 2
    if ghost.Ghost.HEALTH >= main_screen.MAX_NUMBER:
        ghost.Ghost.HEALTH = main_screen.MAX_NUMBER / 2
    if golem.Golem.HEALTH >= main_screen.MAX_NUMBER:
        golem.Golem.HEALTH = main_screen.MAX_NUMBER / 2
    if goblin.Goblin.HEALTH >= main_screen.MAX_NUMBER:
        goblin.Goblin.HEALTH = main_screen.MAX_NUMBER / 2
    if chicken.Chicken.HEALTH >= main_screen.MAX_NUMBER:
        chicken.Chicken.HEALTH = main_screen.MAX_NUMBER / 2

def freeze_potion_activation(): # ефекта на freeze potion-a
    if main_screen.coins < main_screen.FREEZE_POTION_COST:
        return None
    main_screen.coins -= main_screen.FREEZE_POTION_COST
    for enemy in main_screen.enemy_group:
        Snow_animation(enemy.positionX, enemy.positionY)
        enemy.move_x = int(enemy.move_x/2)
        enemy.move_y = int(enemy.move_y/2)

def damage_potion_activation(): # ефекта на damage potion-a
    if main_screen.coins < main_screen.DAMAGE_POTION_COST:
        return None
    main_screen.coins -= main_screen.DAMAGE_POTION_COST
    for enemy in main_screen.enemy_group:
        Blood_animation(enemy.positionX, enemy.positionY)
        enemy.health *= main_screen.DAMAGE_POTION_MULTIPLIER 

    


    