import pygame
import time
import random

from menus import Menus

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

bg = pygame.image.load('images/background.jpg')

game_running = True
menu_control = Menus()
menu_control.main_menu()
status = 'Main Menu'

while game_running:
    old_status = status
    clock.tick(60)
    screen.blit(bg, (0, 0))
    # screen.fill('black')
    menu_control.blit_menu(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if status == 'Main Menu':
                    button_list = menu_control.to_blit
                    if button_list[0].rect.collidepoint(*pygame.mouse.get_pos()):
                        status = 'Start Game'
                        menu_control.start_game()
                    elif button_list[1].rect.collidepoint(*pygame.mouse.get_pos()):
                        status = 'Controls'
                        menu_control.controls_menu()

    if status != old_status:
        print(f'New Status: {old_status} --> {status}')

    pygame.display.update()
