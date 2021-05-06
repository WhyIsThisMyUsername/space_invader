import pygame

from menu_controller import MenuController

pygame.init()

GAME_SIZE = (1280, 960)
SCREEN = pygame.display.set_mode(GAME_SIZE)

MENU_CONTROLLER = MenuController(GAME_SIZE)
MENU_STATUSES = ('Main Menu', 'Control Menu', 'Bouncing Button')

clock = pygame.time.Clock()
game_running = True
status = 'Main Menu'

MENU_CONTROLLER.main_menu()

while game_running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if status == 'Main Menu':
                    mouse_pos = (*pygame.mouse.get_pos(),)
                    button_list = MENU_CONTROLLER.return_buttons()
                    if button_list[0].return_rect().collidepoint(mouse_pos):
                        print('CLICK START')
                    elif button_list[1].return_rect().collidepoint(mouse_pos):
                        pass
                        # status = 'Controls'
                    elif button_list[2].return_rect().collidepoint(mouse_pos):
                        status = 'Bouncing Button'
                        MENU_CONTROLLER.bouncing_button_menu()
                
                if status == 'Bouncing Button':
                    mouse_pos = (*pygame.mouse.get_pos(),)
                    button_list = MENU_CONTROLLER.return_bouncing_buttons()
                    if button_list[0].return_rect().collidepoint(mouse_pos):
                        MENU_CONTROLLER.main_menu()
                        status = 'Main Menu'
    if status == 'Bouncing Button':
        MENU_CONTROLLER.bouncing_button_update()
    
    if status in MENU_STATUSES:
        SCREEN.blit(MENU_CONTROLLER.return_screen(), (0, 0))
    elif status.startswith('Level'):
        pass
    
    pygame.display.update()
