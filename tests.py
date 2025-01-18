# unit test-ове на проекта

import unittest
import enemy
import water_attack # ще използвам water_attack, защото няма значение точно коя атака ползвам, тъй като всички ползват общ базов клас


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


if __name__ == "__main__":
    unittest.main()
        

