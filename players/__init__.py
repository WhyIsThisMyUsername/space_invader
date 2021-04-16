import pygame


class Player:
    def __init__(self):
        self.lives = 3
        self.health = 100
        self.firing_speed = 1
        self.multi_shot = 1
        self.active_powers = []
        
        self.sprite = pygame.image.load('images/player.png')
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
