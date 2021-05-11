# Imports
import pygame
from bullet import Bullet

# Initializing pygame
pygame.init()


# "Imports" Bullet class and bases PlayerBullet class off of it
class PlayerBullet(Bullet):
    # Initializes Bullet class and sets player bullet color and direction
    def __init__(self, pos, speed):
        super().__init__(pos, speed)
        self._sprite.fill('white')
        self._bullet_direction = -5
    
    # Checks if bullet is colliding with an enemy
    def collision_check(self, enemy):
        if self.return_rect().colliderect(enemy):
            return True
