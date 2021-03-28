import pygame
import time
import random

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))

bg = pygame.image.load('images/background.jpg')


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
        self.small_button_font = pygame.font.SysFont('Corbel', 35)

    def main_menu(self):



game_running = True
while game_running:
    clock.tick(60)
    screen.blit(bg, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_over = True
