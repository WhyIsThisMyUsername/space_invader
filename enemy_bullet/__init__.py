# Imports
import pygame
from bullet import Bullet

# Initializes pygame
pygame.init()


# "Imports" Bullet class as base for EnemyBullet class
class EnemyBullet(Bullet):
    # Initializes bullet class and sets enemy bullet color and direction
    def __init__(self, pos, speed):
        super().__init__(pos, speed)
        self._sprite.fill('red')
        self._bullet_direction = 5
    
    # Checks if bullet is colliding with the player#
    def collision_check(self, player):
        if self.return_rect().colliderect(player):
            return True
