import pygame
from menu_components import Button
from menu_components import ResizingText
from players import Player

pygame.init()

large_button_font = pygame.font.SysFont('Corbel', 70)
medium_button_font = pygame.font.SysFont('Corbel', 35)


class Menus:
    def __init__(self, screen):
        self.screen = screen
        self.to_blit_buttons = []
        self.to_blit_resizing_text = []
    
    def main_menu(self):
        self.to_blit_buttons = []
        self.to_blit_resizing_text = []
        self.to_blit_buttons.append(Button('Start', (320, 100), (15, 15, 15), 'white', large_button_font))
        self.to_blit_buttons.append(Button('Controls', (320, 200), (15, 15, 15), 'white', large_button_font))
        self.to_blit_buttons.append(Button('Bouncy', (320, 300), (15, 15, 15), 'white', large_button_font))
    
    def controls_menu(self):
        self.to_blit_buttons = []
        self.to_blit_resizing_text = []
        controls_text = 'insert\ncontrols\nhere'
        self.to_blit_buttons.append(Button('Return', (580, 430), (15, 15, 15), 'white', medium_button_font))
        self.to_blit_resizing_text.append(
            ResizingText(self.screen, controls_text, (50, 50), (620, 540), 'white', (15, 15, 15), medium_button_font))

    def bouncing_button_demo(self):
        self.to_blit_buttons = []
        self.to_blit_resizing_text = []
        self.to_blit_buttons.append(Button('BOUNCE', (320, 400), (15, 15, 15), 'white', medium_button_font))
    
    def start_game(self):
        self.to_blit_buttons = []
        self.to_blit_resizing_text = []
        
    def blit_menu(self):
        for i in self.to_blit_resizing_text:
            self.screen.blit(i.new_surface, (0, 0))
        
        for i in self.to_blit_buttons:
            self.screen.blit(i.surface, (i.middle_x, i.middle_top_y))
