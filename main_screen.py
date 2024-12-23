import pygame

pygame.init()

attacks_group = pygame.sprite.Group()
troops_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
checkpoints = [210, 400, 655, 640, 960]
castle_health = 5
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 680
GAME_NAME = "Defend the summit"
MAX_FRAMERATE = 60
TOLERANCE = 25
ATTACK_MOVEMENT_ADDITION = 4
current_round = 1
cycles_count = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()
main_back = pygame.image.load("Images/Backgrounds/main_path.png")

def get_closest_enemy():
    sprites = enemy_group.sprites()
    if len(sprites) == 0:
        return None
    max_distance = sprites[0].travelled_distance
    closest_enemy = sprites[0]
    for sprite in sprites:
        if sprite.travelled_distance > max_distance:
            max_distance = sprite.travelled_distance
            closest_enemy = sprite
    return closest_enemy