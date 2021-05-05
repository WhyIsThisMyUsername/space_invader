import pygame

pygame.init()


class Button:
    def __init__(self, text, pos, colors, font):
        x, self._y = pos
        text_color, bg_color = colors
        text_size = font.render(text, True, pygame.Color(text_color)).get_size()
        self._middle_x = int((x - text_size[0] / 2) // 1)
        self.set_text(text, colors, font)

    def set_text(self, text, colors, font):
        text_color, bg_color = colors
        self._text = font.render(text, True, pygame.Color(text_color))
        self._text_size = self._text.get_size()
        self._surface = pygame.Surface(self._text_size)
        self._surface.fill(bg_color)
        self._surface.blit(self._text, (0, 0))
        self._rect = pygame.Rect(self._middle_x, self._y, *self._text_size)

    def return_text(self):
        return self._surface

    def return_rect(self):
        return self._rect

    def return_coords(self):
        return self._middle_x, self._y
