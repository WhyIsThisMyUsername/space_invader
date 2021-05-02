import pygame


class Player:
    def __init__(self, x, y):
        self.lives = 3
        self.health = 100
        self.firing_speed = 1
        self.multi_shot = 1
        self.active_powers = []
        
        self.sprite = pygame.image.load('images/player.png')
        self.sprite = pygame.transform.scale(self.sprite, (70, 70))

        self.rect = pygame.Rect(x, y, 70, 70)
        
        self.x = x
        self.y = y
