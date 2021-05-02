import pygame
import time
import random

from menus import Menus
from levels import LevelController

pygame.init()

large_button_font = pygame.font.SysFont('Corbel', 70)
medium_button_font = pygame.font.SysFont('Corbel', 35)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 960))

bg = pygame.image.load('images/background.jpg')
bg = pygame.transform.scale(bg, (1280, 960))

game_running = True
menu_control = Menus(screen)
level_control = LevelController(screen, 1280, 960)
menu_control.main_menu()
status = 'Main Menu'
direction = ['up', 20]
left_held, right_held, fire_held = False, False, False
fire_speed = 60

while game_running:
    old_status = status
    clock.tick(60)
    screen.blit(bg, (0, 0))
    
    if status.startswith('Level'):
        level_control.blit_screen()
    else:
        menu_control.blit_menu()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        
        # Include additional IF statement to check if status != levels?
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if status == 'Main Menu':
                    button_list = menu_control.to_blit_buttons
                    if button_list[0].rect.collidepoint(*pygame.mouse.get_pos()):
                        status = 'Level one'
                        level_control.load_level_one()
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left_held = True
                if event.key == pygame.K_RIGHT:
                    right_held = True
                if event.key == pygame.K_SPACE:
                    fire_held = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_held = False
                if event.key == pygame.K_RIGHT:
                    right_held = False
                if event.key == pygame.K_SPACE:
                    fire_held = False
    
    if status.startswith('Level'):
        if left_held and not level_control.player.x < 70:
            level_control.player.x -= 10
        
        if right_held and not level_control.player.x > 1210:
            level_control.player.x += 10
        
        if fire_speed < 100:
            fire_speed += 1
        
        if fire_held:
            if fire_speed >= 30:
                level_control.player_fire_bullet()
                fire_speed = 0
    
    if status == 'Bouncing Button':
        if direction[0] == 'up' and direction[1] == 21:
            direction[1] = 20
        if direction[0] == 'up':
            menu_control.to_blit_buttons[0].middle_top_y -= direction[1]
            menu_control.to_blit_buttons[0].rect = menu_control.to_blit_buttons[0].rect.move(0, -direction[1])
            direction[1] -= 1
            if direction[1] == 0:
                direction[0] = 'down'
                print(menu_control.to_blit_buttons[0].middle_top_y)
        elif direction[0] == 'down':
            menu_control.to_blit_buttons[0].middle_top_y += direction[1]
            menu_control.to_blit_buttons[0].rect = menu_control.to_blit_buttons[0].rect.move(0, direction[1])
            direction[1] += 1
            if direction[1] == 21:
                direction[0] = 'up'
                print(menu_control.to_blit_buttons[0].middle_top_y)
    
    if status != old_status:
        print(f'New Status: "{old_status}" --> "{status}"')
    
    pygame.display.update()
