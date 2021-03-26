import pygame
import time
import random

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))

bg = pygame.image.load('images/background.jpg')

game_running = True
while game_running:
    clock.tick(60)
    screen.blit(bg, (0, 0))
    pygame.display.update()
