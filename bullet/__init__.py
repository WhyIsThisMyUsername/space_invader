# Imports
import pygame

# Initializing pygame
pygame.init()


# Creates bullet class to base player and enemy bullet classes on
class Bullet:
    # Sets sprites, hitbox, position, and movement speed (direction is reset later)
    def __init__(self, pos, speed):
        self._bullet_x, self._bullet_y = pos
        self._rect = pygame.Rect(self._bullet_x, self._bullet_y, 10, 20)
        self._sprite = pygame.Surface((5, 10))
        self._bullet_progress = 0
        self._bullet_speed = speed
        self._bullet_direction = 0
    
    # Updates bullet
    def update_bullet(self):
        self._bullet_progress += 1
        if self._bullet_progress >= self._bullet_speed:
            self._move_bullet()
            self._bullet_progress = 0
    
    # Moves bullet
    def _move_bullet(self):
        self._rect = self._rect.move(0, self._bullet_direction)
        self._bullet_y += self._bullet_direction
    
    # Checks if the bullet is off screen
    def invalid_position(self):
        if not 0 < self._bullet_y < 960:
            return True
    
    # Returns the hitbox
    def return_rect(self):
        return self._rect
    
    # Returns the sprite
    def return_sprite(self):
        return self._sprite
    
    # Returns the position
    def return_pos(self):
        return self._bullet_x, self._bullet_y
