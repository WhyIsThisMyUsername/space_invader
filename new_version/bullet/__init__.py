import pygame

pygame.init()


class Bullet:
    def __init__(self, pos, speed):
        self._bullet_x, self._bullet_y = pos
        self._rect = pygame.Rect(self._bullet_x, self._bullet_y, 10, 20)
        self._sprite = pygame.Surface((5, 10))
        self._bullet_progress = 0
        self._bullet_speed = speed
        self._bullet_direction = 0
    
    def update_bullet(self):
        self._bullet_progress += 1
        if self._bullet_progress >= self._bullet_speed:
            self._move_bullet()
            self._bullet_progress = 0
    
    def _move_bullet(self):
        self._rect = self._rect.move(0, self._bullet_direction)
        self._bullet_y += self._bullet_direction
    
    def invalid_position(self):
        if not 0 < self._bullet_y < 960:
            return True
    
    def return_rect(self):
        return self._rect
    
    def return_sprite(self):
        return self._sprite
    
    def return_pos(self):
        return self._bullet_x, self._bullet_y
