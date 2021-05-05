import pygame

from menu_controller import MenuController

pygame.init()

GAME_SIZE = (1280, 960)
SCREEN = pygame.display.set_mode(GAME_SIZE)
BG = pygame.transform.scale(pygame.image.load('images/background.jpg'), (1280, 960))

MENU_CONTROLLER = MenuController(GAME_SIZE)

clock = pygame.time.Clock()
game_running = True
status = 'Main Menu'

MENU_CONTROLLER.main_menu()

while game_running:
    clock.tick(60)
    SCREEN.blit(BG, (0, 0))
