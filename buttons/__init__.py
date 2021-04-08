import pygame

pygame.init()

large_button_font = pygame.font.SysFont('Corbel', 70)
medium_button_font = pygame.font.SysFont('Corbel', 35)


class Button:
    def __init__(self, text, x, y, bg_color, text_color):
        self.middle_x = x
        self.middle_top_y = y
        self.set_text(text, bg_color, text_color)
    
    def set_text(self, text, button_bg, text_color):
        self.text = large_button_font.render(text, True, pygame.Color(text_color))
        self.text_size = self.text.get_size()
        self.surface = pygame.Surface(self.text_size)
        self.surface.fill(button_bg)
        self.surface.blit(self.text, (0, 0))
        # self.surface.set_alpha(100)
        self.middle_x = self.middle_x - self.text_size[0] / 2
        self.rect = pygame.Rect(self.middle_x,
                                self.middle_top_y,
                                self.text_size[0],
                                self.text_size[1])
