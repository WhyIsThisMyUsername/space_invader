import pygame

pygame.init()

class Bullet:
    bullet_speed = 1
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 5, 10)
        self.x = x
        self.y = y
        self.sprite = pygame.Surface((5, 10))
        self.sprite.fill('white')
        self.bullet_progress = 0