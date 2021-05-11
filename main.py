# Imports
import pygame

from menu_controller import MenuController
from level_controller import LevelController

# Initializes pygame
pygame.init()

# Creates game screen
GAME_SIZE = (1280, 960)
SCREEN = pygame.display.set_mode(GAME_SIZE)

# Creates controller and statuses for the menus
MENU_CONTROLLER = MenuController(GAME_SIZE)
MENU_STATUSES = ('Main Menu', 'Controls', 'Bouncing Button', 'End Screen')
status = 'Main Menu'

# Creates controller for levels
LEVEL_CONTROLLER = LevelController((1280, 960))

# Creates FPS clock, runs the game, and sets movement and firing of player to false
clock = pygame.time.Clock()
game_running = True
left_held, right_held, fire_held = False, False, False

# Changes menu to main menu
MENU_CONTROLLER.main_menu()

while game_running:
    # Limits FPS and keeps track of status changes
    clock.tick(60)
    old_status = status
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        
        # Checks which buttons are pressed and changes menus/controllers (if starting/ending game)
        # based on what menu is active
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if status == 'Main Menu':
                    mouse_pos = (*pygame.mouse.get_pos(),)
                    button_list = MENU_CONTROLLER.return_buttons()
                    if button_list[0].return_rect().collidepoint(mouse_pos):
                        LEVEL_CONTROLLER.load_level_one()
                        status = 'Level one'
                    elif button_list[1].return_rect().collidepoint(mouse_pos):
                        status = 'Controls'
                        MENU_CONTROLLER.controls_menu()
                    elif button_list[2].return_rect().collidepoint(mouse_pos):
                        status = 'Bouncing Button'
                        MENU_CONTROLLER.bouncing_button_menu()
                elif status == 'Controls':
                    mouse_pos = (*pygame.mouse.get_pos(),)
                    button_list = MENU_CONTROLLER.return_buttons()
                    if button_list[0].return_rect().collidepoint(mouse_pos):
                        MENU_CONTROLLER.main_menu()
                        status = 'Main Menu'
                elif status == 'Bouncing Button':
                    mouse_pos = (*pygame.mouse.get_pos(),)
                    button_list = MENU_CONTROLLER.return_bouncing_buttons()
                    if button_list[0].return_rect().collidepoint(mouse_pos):
                        MENU_CONTROLLER.main_menu()
                        status = 'Main Menu'
                elif status == 'End Screen':
                    mouse_pos = (*pygame.mouse.get_pos(),)
                    button_list = MENU_CONTROLLER.return_buttons()
                    if button_list[0].return_rect().collidepoint(mouse_pos):
                        MENU_CONTROLLER.main_menu()
                        status = 'Main Menu'
        
        # Updates what movement/firing keys are pressed/depressed
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
    
    # Moves the player and checks if the game is won or lost
    # Also switches to menu controller instead of level controller if game won/lost
    if status.startswith('Level'):
        if left_held:
            LEVEL_CONTROLLER.move_player('left')
        if right_held:
            LEVEL_CONTROLLER.move_player('right')
        if fire_held:
            LEVEL_CONTROLLER.player_fire()
        
        if LEVEL_CONTROLLER.return_status() == 'Victory':
            status = 'End Screen'
            MENU_CONTROLLER.victory_screen()
        
        elif LEVEL_CONTROLLER.return_status() == 'Defeat':
            status = 'End Screen'
            MENU_CONTROLLER.defeat_screen()
    
    # Updates the bouncing button if menu is set to bouncing button
    if status == 'Bouncing Button':
        MENU_CONTROLLER.bouncing_button_update()
    
    # Runs the correct graphics controller based on the status
    if status in MENU_STATUSES:
        SCREEN.blit(MENU_CONTROLLER.return_screen(), (0, 0))
    elif status.startswith('Level'):
        LEVEL_CONTROLLER.update_game()
        SCREEN.blit(LEVEL_CONTROLLER.return_screen(), (0, 0))
    
    # Keeps track of any status changes and prints a notification if the status changed
    if status != old_status:
        print(f'{old_status} --> {status}')
    
    # Updates the display
    pygame.display.update()
