import pygame

pygame.init()

class Enemy:
    def __init__(self, image_array, x, y):
        self.sprites = image_array
        self.x, self.y = x, y
        self.rect = pygame.Rect(x, y, *self.sprites[0].get_size())
