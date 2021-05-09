import pygame
from new_version.bullet import Bullet

pygame.init()


class EnemyBullet(Bullet):
    def __init__(self, pos, speed):
        super().__init__(pos, speed)
        self._sprite.fill('red')
        self._bullet_movement = 5
    
    def collision_check(self, player):
        if self._rect.colliderect(player.get_hitbox()):
            pass
