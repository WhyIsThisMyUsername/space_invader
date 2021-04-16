import pygame
import time
import random

from menus import Menus
from players import Player

pygame.init()

large_button_font = pygame.font.SysFont('Corbel', 70)
medium_button_font = pygame.font.SysFont('Corbel', 35)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))

bg = pygame.image.load('images/background.jpg')

player = Player()

game_running = True
menu_control = Menus(screen)
menu_control.main_menu()
status = 'Main Menu'
direction = ['up', 20]

while game_running:
    old_status = status
    clock.tick(30)
    screen.blit(bg, (0, 0))

    if status.startswith('Level'):
        menu_control.blit_menu(levels=True)
    else:
        menu_control.blit_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if status == 'Main Menu':
                    button_list = menu_control.to_blit_buttons
                    if button_list[0].rect.collidepoint(*pygame.mouse.get_pos()):
                        status = 'Start Game'
                        menu_control.start_game()
                    elif button_list[1].rect.collidepoint(*pygame.mouse.get_pos()):
                        status = 'Controls'
                        menu_control.controls_menu()
                    elif button_list[2].rect.collidepoint(*pygame.mouse.get_pos()):
                        status = 'Bouncing Button'
                        menu_control.bouncing_button_demo()
                elif status == 'Controls':
                    button_list = menu_control.to_blit_buttons
                    if button_list[0].rect.collidepoint(*pygame.mouse.get_pos()):
                        status = 'Main Menu'
                        menu_control.main_menu()
                elif status == 'Bouncing Button':
                    button_list = menu_control.to_blit_buttons
                    if button_list[0].rect.collidepoint(*pygame.mouse.get_pos()):
                        status = 'Main Menu'
                        direction = ['up', 20]
                        menu_control.main_menu()

        if status.startswith('Level'):
            if event.type == pygame.K_LEFT:
                pass

    if status == 'Bouncing Button':
        if direction[0] == 'up' and direction[1] == 21:
            direction[1] = 20
        if direction[0] == 'up':
            menu_control.to_blit_buttons[0].middle_top_y -= direction[1]
            # menu_control.to_blit_buttons[0].rect = menu_control.to_blit_buttons[0].rect.move(0, -direction[1])
            direction[1] -= 1
            if direction[1] == 0:
                direction[0] = 'down'
                print(menu_control.to_blit_buttons[0].middle_top_y)
        elif direction[0] == 'down':
            menu_control.to_blit_buttons[0].middle_top_y += direction[1]
            menu_control.to_blit_buttons[0].set_text('BOUNCE', (15, 15, 15), 'white', medium_button_font)
            # menu_control.to_blit_buttons[0].rect = menu_control.to_blit_buttons[0].rect.move(0, direction[1])
            direction[1] += 1
            if direction[1] == 21:
                direction[0] = 'up'
                print(menu_control.to_blit_buttons[0].middle_top_y)

    if status != old_status:
        print(f'New Status: "{old_status}" --> "{status}"')

    pygame.display.update()
