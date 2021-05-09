import pygame

pygame.init()

class Player:
    def __init__(self, pos):
        self._player_x, self._player_y = pos
        self._lives = 3
        self._firing_speed = 40
        self._bullet_cooldown = 0
        
        self._sprite = pygame.image.load('images/player.png')
        self._sprite = pygame.transform.scale(self._sprite, (140, 140))
        
        self._rect = pygame.Rect(self._player_x, self._player_y, (140, 140))
    
    def