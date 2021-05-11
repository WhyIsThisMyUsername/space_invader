import pygame
from new_version.bullet import Bullet

pygame.init()

class PlayerBullet(Bullet):
    def __init__(self, pos, speed):
        super().__init__(pos, speed)
        self._sprite.fill('white')
        self._bullet_direction = -5

    def collision_check(self, enemy):
        if self.return_rect().colliderect(enemy):
            return True
