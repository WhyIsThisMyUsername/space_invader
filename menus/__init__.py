import pygame
from buttons import Button

pygame.init()


class Menus:
    def __init__(self):
        self.to_blit = []
    
    def main_menu(self):
        self.to_blit = []
        self.to_blit.append(Button('Start', 320, 100, (15, 15, 15), 'white'))
        self.to_blit.append(Button('Controls', 320, 200, (15, 15, 15), 'white'))

    def controls_menu(self):
        self.to_blit = []
        self.to_blit.append(Button('Return', 580, 430, (15, 15, 15), 'white'))

    def start_game(self):
        pass
    
    def blit_menu(self, screen):
        for i in self.to_blit:
            screen.blit(i.surface, (i.middle_x, i.middle_top_y))
