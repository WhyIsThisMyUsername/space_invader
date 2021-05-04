import pygame
from new_version.button import Button

pygame.init()

class BouncingButton:
    def __init__(self, text, starting_pos, colors, font):
        self._starting_x, self._starting_y = starting_pos
        text_color, bg_color = colors
        text = font.render(text, True, text_color)
        self._bg = pygame.Surface(text.get_size()).fill(bg_color)
        self.reset_coordinates()

    def reset_coordinates(self):
        self._current_x = self._starting_x - self._bg.get_size()[0] / 2
        self._current_y = self._starting_y