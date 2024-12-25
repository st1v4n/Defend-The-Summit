import pygame

pygame.init()

attacks_group = pygame.sprite.Group()
troops_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
animations_group = pygame.sprite.Group()
buttons_group = pygame.sprite.Group()
lifes_group = pygame.sprite.Group()
button_pressed_group = pygame.sprite.Group()
black_color = (0, 0, 0)
main_font = pygame.font.Font(None, 24)
checkpoints = [210, 400, 655, 640, 960]
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 680
GAME_NAME = "Defend the summit"
MAX_FRAMERATE = 60
TOLERANCE = 25
TEXT_DISPLAY = 50
ATTACK_MOVEMENT_ADDITION = 4
DEFAULT_SPAWN_X = 1000
DEFAULT_SPAWN_Y = 30
TROOP_COST = 50
TROOPS_COUNT = 4
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 80
game_started = False
cycles_count = 0
zombie_spawn_count = 0
coins = 300
button_pressed = None

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()
main_back = pygame.image.load("Images/Backgrounds/main_path.png")

