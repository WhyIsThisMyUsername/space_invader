import pygame
import random

pygame.init()


class Enemy:
    bullet_chance = 20
    def __init__(self, image_array, x, y):
        self.bullet_delay = 60
        self.bullet_charge = 0
        self.sprites = image_array
        self.x, self.y = x, y
        self.rect = pygame.Rect(x, y, *self.sprites[0].get_size())
    
    def fire_bullet_check(self):
        if self.bullet_charge < self.bullet_delay:
            self.bullet_charge += 1
        if self.bullet_charge >= self.bullet_delay:
            number = random.randint(0, self.bullet_chance)
            if number == 1:
                return True
            self.bullet_charge = 0
        return False
