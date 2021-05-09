import pygame
import random
from new_version.enemy_bullet import EnemyBullet

pygame.init()
DISPLAY_X =

class Enemy:
    _bullet_chance = 20
    _bullet_list = []
    _bullet_delay = 60
    _enemy_list = []
    _animation_speed = 30
    _animation_charge = 0
    _going_left = True

    def __init__(self, pos, images):
        self._bullet_charge = 0
        self._sprites = images
        self._enemy_x, self._enemy_y = pos
        self.rect = pygame.Rect(self._enemy_x, self._enemy_y, *self._sprites[0].get_size())

    def fire_bullet_check(self):
        if self._bullet_charge < self._bullet_delay:
            self._bullet_charge += 1
        if self._bullet_charge >= self._bullet_delay:
            self._bullet_charge = 0
            if not random.randint(0, self._bullet_chance):
                return True
        return False

    def _fire_bullet(self):
        self._bullet_list.append(EnemyBullet((self._enemy_x + 35, self._enemy_y + 70), 1))

    def update_bullet(self):
        for bullet in self._bullet_list:
            bullet.update_bullet()

    def update_enemies(self):
        self._animation_charge += 1
        if self._animation_charge >= self._animation_speed:

    def generate_enemies(self, level):
        if level == 1:
            working_size = (480, )