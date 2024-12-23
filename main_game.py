from sys import exit
import main_screen
import fish_troop
import zombie
import ghost

fish = fish_troop.Fish_troop(10, 20, 900, 120)
fish = fish_troop.Fish_troop(10, 40, 900, 240)
zombie = zombie.Zombie(1000, 30)
ghost = ghost.Ghost(1100, 30)
def main_loop():
    while True:
        for event in main_screen.pygame.event.get():
            if event.type == main_screen.pygame.QUIT:
                main_screen.pygame.quit()
                exit()
        main_screen.screen.blit(main_screen.main_back, (0,0))
        main_screen.enemy_group.update()
        main_screen.enemy_group.draw(main_screen.screen)
        main_screen.troops_group.draw(main_screen.screen)
        enemy_to_attack = main_screen.get_closest_enemy()
        if enemy_to_attack is not None:
            main_screen.troops_group.update(main_screen.cycles_count)
            main_screen.attacks_group.update(enemy_to_attack)
            main_screen.attacks_group.draw(main_screen.screen)
        main_screen.pygame.display.update()
        main_screen.cycles_count += 1
        main_screen.cycles_count %= 1000 
        main_screen.clock.tick(main_screen.MAX_FRAMERATE)

main_loop()
