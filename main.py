import pygame
import time
import random

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))

bg = pygame.image.load('images/background.jpg')
button_font = pygame.font.SysFont('Corbel', 35)

class Player():
    def __init__(self):
        self.lives = 3
        self.health = 100
        self.firing_speed = 1
        self.multi_shot = 1
        self.active_powerups = []

        self.sprite = pygame.image.load('images/player.png')


class Enemy():
    pass


class Menus():
    def __init__(self):


    def main_menu(self):


class Button():
    def __init__(self, text, x, y, bg_color, text_color):
        self.middle_x = x
        self.middle_top_y = y
        self.text_color = text_color
        self.text = self.set_text(text, bg_color, self.middle_x, self.middle_top_y, self.text_color)

    def set_text(self, text, bg, x, y, text_color):
        self.text = button_font.render(text, True, pygame.color(text_color))
        self.text_size = self.text.get_size()
        self.surface = pygame.Surface(self.text_size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(x - self.text_size[0] / 2)

game_running = True
while game_running:
    clock.tick(60)
    screen.blit(bg, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_over = True
