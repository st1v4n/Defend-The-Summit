from sys import exit
import main_screen
import logics
import buttons
import lifepoint

# генерираме трите си бутона
buttons.Buy_button(1100, 600)
buttons.Upgrade_button(1100, 480)
buttons.Max_upgrade_button(1100, 360)
# генерираме potion-ните
buttons.Freeze_potion_button(50, 620)
buttons.Damage_potion_button(150, 620)
# по 3 живота
lifepoint.Life(855, 340)
lifepoint.Life(910, 340)
lifepoint.Life(965, 340)


def main_loop():
    while True:
        for event in main_screen.pygame.event.get():
            if event.type == main_screen.pygame.QUIT:
                main_screen.pygame.quit()
                exit()
            if event.type == main_screen.pygame.MOUSEBUTTONUP: # при натискане на мишката
                if main_screen.button_pressed is None: # дали преди това е била натисната
                    mouseCord = main_screen.pygame.mouse.get_pos()
                    for button in main_screen.buttons_group:
                        if button.validate(mouseCord[0], mouseCord[1]): # ако натискането отговаря на бутон
                            main_screen.button_pressed = button
                            main_screen.button_pressed.animation = buttons.Button_Press_animation(button.positionX, button.positionY)
                            break
                else: # ако вече е натиснат бутон, избираме на каква локация да се приложи неговото действие
                    mouseCord = main_screen.pygame.mouse.get_pos()
                    main_screen.button_pressed.update(mouseCord[0], mouseCord[1])
                    main_screen.button_pressed.animation.kill()
                    main_screen.button_pressed = None
            if event.type == main_screen.pygame.KEYDOWN: # чудовища започват да се spawn-ват, когато се натисне бутона 's' на клавиатурата 
                if event.key == main_screen.pygame.K_s:
                    main_screen.game_started = True
        main_screen.screen.blit(main_screen.main_back, (0,0))
        main_screen.buttons_group.draw(main_screen.screen)
        logics.display_coin_situation()
        if main_screen.game_started:
            logics.spawn_enemy()
        else:
            to_start_text = main_screen.main_font.render("Press 's' key to start!", True, main_screen.black_color)
            rectangle_start_text = to_start_text.get_rect()
            rectangle_start_text.center = (1100, 120)
            main_screen.screen.blit(to_start_text, rectangle_start_text)
        main_screen.enemy_group.update()
        main_screen.enemy_group.draw(main_screen.screen)
        main_screen.troops_group.update(main_screen.cycles_count)
        main_screen.troops_group.draw(main_screen.screen)
        enemy_to_attack = logics.get_closest_enemy()
        if enemy_to_attack is not None:
            main_screen.attacks_group.update(enemy_to_attack)
            main_screen.attacks_group.draw(main_screen.screen)
        main_screen.animations_group.update()
        main_screen.animations_group.draw(main_screen.screen)
        main_screen.lifes_group.update()
        main_screen.lifes_group.draw(main_screen.screen)
        main_screen.button_pressed_group.draw(main_screen.screen)
        main_screen.pygame.display.update()
        main_screen.cycles_count += 1
        main_screen.cycles_count %= 1000
        main_screen.enemy_spawn_count += 1
        if main_screen.enemy_spawn_count >= 5000:
            logics.boost_enemies()
            main_screen.enemy_spawn_count = 1
        main_screen.clock.tick(main_screen.MAX_FRAMERATE)

main_loop()
