import pygame

pygame.init()

large_button_font = pygame.font.SysFont('Corbel', 70)
medium_button_font = pygame.font.SysFont('Corbel', 35)
bg = pygame.image.load('images/background.jpg')


class Button:
    def __init__(self, text, pos, bg_color, text_color, font):
        self.middle_x, self.middle_top_y = pos
        self.text_size = font.render(text, True, pygame.Color(text_color)).get_size()
        self.middle_x = self.middle_x - self.text_size[0] / 2
        self.set_text(text, bg_color, text_color, font)
    
    def set_text(self, text, button_bg, text_color, font):
        self.text = font.render(text, True, pygame.Color(text_color))
        self.text_size = self.text.get_size()
        self.surface = pygame.Surface(self.text_size)
        self.surface.fill(button_bg)
        self.surface.blit(self.text, (0, 0))
        # self.surface.set_alpha(100)
        self.rect = pygame.Rect(self.middle_x,
                                self.middle_top_y,
                                self.text_size[0],
                                self.text_size[1])
        

class ResizingText:
    def __init__(self, surface, text, pos, max_pos, text_color, bg_color, font):
        self.render_text(surface, text, pos, max_pos, text_color, bg_color, font)
    
    def render_text(self, surface, text, pos, max_pos, text_color, bg_color, font):
        space = font.size(' ')[0]
        words = [sentence.split(' ') for sentence in text.splitlines()]
        x, y = pos
        max_x, max_y = max_pos
        self.new_surface = pygame.Surface(surface.get_size())
        self.new_surface.blit(bg, (0, 0))
        for line in words:
            for word in line:
                text_surface = font.render(word, 1, text_color)
                background_surface = pygame.Surface(text_surface.get_size())
                background_surface.fill(bg_color)
                background_surface.blit(text_surface, (0, 0))
                word_width, word_height = background_surface.get_size()
                if x + word_width > max_x:
                    x = pos[0]
                    y += word_height
                self.new_surface.blit(background_surface, (x, y))
                x += word_width + space
            x = pos[0]
            y += word_height