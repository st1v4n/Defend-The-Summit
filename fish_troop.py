"""Рибата"""
import troop
import main_screen
from water_attack import Water_attack

fish_path_name = "Images/Troops/fish_troop.png"

class Fish_troop(troop.Troop):

    def __init__(self, attack_damage, attack_speed, positionX, positionY):
        troop.Troop.__init__(self, attack_damage, attack_speed, positionX, positionY)
        self.image = main_screen.pygame.image.load(fish_path_name)
        self.rect = self.image.get_rect()
        self.rect.center = (self.positionX, self.positionY)
        main_screen.troops_group.add(self)

    def update(self, cycles_count):
        if cycles_count % self.attack_delay == 0:
            self.attack = Water_attack(self.positionX, self.positionY, self.level)

        


