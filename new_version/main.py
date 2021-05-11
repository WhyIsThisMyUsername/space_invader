import pygame

from new_version.menu_controller import MenuController
from new_version.level_controller import LevelController

pygame.init()

GAME_SIZE = (1280, 960)
SCREEN = pygame.display.set_mode(GAME_SIZE)

MENU_CONTROLLER = MenuController(GAME_SIZE)
MENU_STATUSES = ('Main Menu', 'Controls', 'Bouncing Button')

LEVEL_CONTROLLER = LevelController((1280, 960))

clock = pygame.time.Clock()
game_running = True
left_held, right_held, fire_held = False, False, False
status = 'Main Menu'

MENU_CONTROLLER.main_menu()

while game_running:
    clock.tick(60)
    old_status = status
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        
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
        if left_held:
            LEVEL_CONTROLLER.move_player('left')
        if right_held:
            LEVEL_CONTROLLER.move_player('right')
        if fire_held:
            LEVEL_CONTROLLER.player_fire()
        
    if status == 'Bouncing Button':
        MENU_CONTROLLER.bouncing_button_update()
    
    if status in MENU_STATUSES:
        SCREEN.blit(MENU_CONTROLLER.return_screen(), (0, 0))
    elif status.startswith('Level'):
        LEVEL_CONTROLLER.update_game()
        SCREEN.blit(LEVEL_CONTROLLER.return_screen(), (0, 0))
    
    if status != old_status:
        print(f'{old_status} --> {status}')
    
    pygame.display.update()
