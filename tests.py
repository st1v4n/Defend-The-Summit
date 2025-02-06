# unit test-ове на проекта

import unittest
import enemy
import water_attack # ще използвам water_attack, защото няма значение точно коя атака ползвам, тъй като всички ползват общ базов клас
import logics
import zombie # няма значение кое enemy зимаме, всички са с еднакъв базов клас, който така или иначе върши цялата работа
import fire_attack
import dark_attack
import light_attack


class Project_tests(unittest.TestCase):

    def setUp(self):
        self.enemy = enemy.Enemy(1000, 30, 100000, -4, 0, "Images/Enemies/chicken.png")

    def test_water_damage_taken(self): # тестваме възможността атаките да правят damage, съответно чудовищата да го поемат
        enemy_health = self.enemy.health
        attack1 = water_attack.Water_attack(self.enemy.positionX, self.enemy.positionY, 1) # 149 + 1*22 = 171
        attack2 = water_attack.Water_attack(self.enemy.positionX, self.enemy.positionY, 2) # 149 + 2*22 = 193
        attack3 = water_attack.Water_attack(self.enemy.positionX, self.enemy.positionY, 3) # 149 + 3*22 = 215
        attack1.update(self.enemy) # първата атака удря, във update на атаките се викат както do_damage() на атаките, така и take_damage на чудовищата
        attack2.update(self.enemy) # втората атака удря 
        attack3.update(self.enemy) # третата атака удря
        expected_damage = 171 + 193 + 215 # damage, който е поел от трите атаки
        expected_health = enemy_health - expected_damage
        self.assertEqual(self.enemy.health, expected_health)
        logics.clean_up()

    def test_water_attack_can_reach_enemy(self): # тестваме дали ако имаме атака от място, различно от позицията на чудовището, ще стигне до него
        attack1 = water_attack.Water_attack(500, 500, 1) # надолу вляво от чудовището
        enemy_health = self.enemy.health
        attack1_start_position = (attack1.positionX, attack1.positionY) # взимаме началната позиция
        attack1.update(self.enemy) # мърдаме атаката
        while attack1_start_position != (attack1.positionX, attack1.positionY): # докато атаката не спре да се движи
            attack1_start_position = (attack1.positionX, attack1.positionY) # мърдаме задния Pointer
            attack1.update(self.enemy) # мърдаме атаката
        expected_health = enemy_health - (water_attack.Water_attack.ATTACK_DAMAGE + 1 * 22) # атаката е спряла да се движи и е ударила
        self.assertEqual(self.enemy.health, expected_health) # проверяваме дали е ударила чудовището
        logics.clean_up()

    def test_enemy_follows_the_path(self): # Тестваме дали чудовището следва направения от мен път, проверявайки дали завива
        direction = self.enemy.get_direction() # В началото посоката на нашата карта е -x
        while direction == self.enemy.get_direction():
            self.enemy.update()
        self.assertEqual(self.enemy.get_direction(), "y")
        direction = self.enemy.get_direction()
        while direction == self.enemy.get_direction():
            self.enemy.update()
        self.assertEqual(self.enemy.get_direction(), "x")
        direction = self.enemy.get_direction()
        while direction == self.enemy.get_direction():
            self.enemy.update()
        self.assertEqual(self.enemy.get_direction(), "y")
        direction = self.enemy.get_direction()
        while direction == self.enemy.get_direction():
            self.enemy.update()
        self.assertEqual(self.enemy.get_direction(), "x")
        logics.clean_up()

    def test_level_up(self): # ще тестваме дали се променя нивото на герой след използване на функционалността Max upgrade
        # както знаем, в играта започваме с 420 coins, което по мой сметки значи, че ако купим един герой на
        # начална цена 20, то ще ни останат 400, които ще стигнат за точно 8 upgrade-a и би трябвало нашия герой
        # да стигне до ниво 9
        new_troop = logics.buy_troop(0, 0)
        logics.max_upgrade(0, 0)
        self.assertEqual(new_troop.level, 9)
        self.assertIsNone(logics.upgrade(0, 0)) # ако нямаме достатъчно пари, функцията връща None
        logics.clean_up()

    def test_enemies_are_boosted(self): # ще тествам дали работи boost_enemies функцията, която прави чудовищата по Здрави и повишава техния spawn rate
        before_zombie = zombie.Zombie(0, 0)
        before_health = before_zombie.get_health()
        before_spawn_rate = before_zombie.get_spawn_rate()
        logics.boost_enemies()
        after_zombie = zombie.Zombie(0, 0)
        self.assertGreater(after_zombie.get_health(), before_health)
        self.assertLess(after_zombie.get_spawn_rate(), before_spawn_rate) # да напомня, че spawn rate представлява delay-я, който трябва да изчакаме докато се spawn-не ново зомби
        before_zombie.kill()
        after_zombie.kill()
        logics.clean_up()

    def test_potion_freeze(self): # проверява дали в действителност нашата freeze potion-ка работи
        before_zombie = zombie.Zombie(1000, 80)
        logics.freeze_potion_activation()
        after_zombie = zombie.Zombie(1000, 80)
        self.assertEqual(before_zombie.get_movement_speed(), int(after_zombie.get_movement_speed()/2))
        logics.clean_up()

    def test_damage_potion(self): # тестваме дали отварата за damage работи
        before_health = self.enemy.get_health()
        logics.damage_potion_activation()
        after_health = self.enemy.get_health() # знаем, че прави 30% от текущия живот
        self.assertAlmostEqual(after_health, before_health - (0.3*before_health))
        logics.clean_up()

    def test_vaporise_reaction(self): # тестваме дали нашата Vaporise реакция работи
        first_attack = fire_attack.Fire_attack(self.enemy.positionX, self.enemy.positionY, 1)
        second_attack = water_attack.Water_attack(self.enemy.positionX, self.enemy.positionY, 1)
        before_health = self.enemy.get_health()
        first_attack.update(self.enemy) # удря първата атака, каято е fire
        second_attack.update(self.enemy) # удря и втората атака, която е water
        # по наши очаквания това трябва да е задействало Vaporise реакция в нашето self.enemy
        after_health = self.enemy.get_health()
        self.assertAlmostEqual(after_health, (before_health - 102 - 171) * 0.85)
        logics.clean_up()

    def test_void_reaction(self): # тестваме дали нашата Void реакция работи
        first_attack = dark_attack.Dark_attack(self.enemy.positionX, self.enemy.positionY, 1)
        second_attack = light_attack.Light_attack(self.enemy.positionX, self.enemy.positionY, 1)
        before_position_x = self.enemy.positionX
        before_position_y = self.enemy.positionY
        first_attack.update(self.enemy)
        second_attack.update(self.enemy)
        # по наши очаквания трябва да се е преместило назад с 15 * 4 пиксела, което е movement speed-a на нашето чудовище, нека видим
        self.assertEqual(abs(before_position_x - self.enemy.positionX), 15 * 4)
        logics.clean_up()
        

if __name__ == "__main__":
    unittest.main()
        

