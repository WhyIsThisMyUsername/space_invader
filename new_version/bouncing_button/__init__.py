import pygame
from new_version.button import Button

pygame.init()

class BouncingButton:
    def __init__(self, text, starting_pos, colors, font):
        self._starting_x, self._starting_y = starting_pos
        text_color, bg_color = colors
        text = font.render(text, True, text_color)
        self._bg = pygame.Surface(text.get_size())
        self._bg.fill(bg_color)
        self._bg.blit(text, (0, 0))
        self._direction = ['up', 30]
        self._hitbox = pygame.Rect(int((self._starting_x - self._bg.get_size()[0] / 2) // 1), self._starting_y, *self._bg.get_size())
        self.reset_coordinates()

    def reset_coordinates(self):
        self._current_x = int((self._starting_x - self._bg.get_size()[0] / 2) // 1)
        self._current_y = self._starting_y
    
    def change_coordinates(self):
        if self._direction[0] == 'up' and self._direction[1] == 31:
            self._direction[1] = 30
        if self._direction[0] == 'up':
            self._current_y -= self._direction[1]
            self._hitbox = self._hitbox.move(0, -self._direction[1])
            self._direction[1] -= 1
            if self._direction[1] == 0:
                self._direction[0] = 'down'
                
        elif self._direction[0] == 'down':
            self._current_y += self._direction[1]
            self._hitbox = self._hitbox.move(0, self._direction[1])
            self._direction[1] += 1
            if self._direction[1] == 31:
                self._direction[0] = 'up'
    
    def return_coordinates(self):
        return self._current_x, self._current_y
    
    def return_rect(self):
        return self._hitbox

    def return_button(self):
        return self._bg
