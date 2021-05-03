import pygame

pygame.init()

LARGE_BUTTON_FONT = pygame.font.SysFont('Corbel', 140)
MEDIUM_BUTTON_FONT = pygame.font.SysFont('Corbel', 70)
BG = pygame.transform.scale(pygame.image.load('images/background.jpg'), (1280, 960))


class Button:
    def __init__(self, text, pos, colors, font):
        x, self.y = pos
        text_color, bg_color = colors
        text_size = font.render(text, True, pygame.Color(text_color)).get_size()
        self.middle_x = x - text_size[0] / 2
        self.set_text(text, colors, font)
    
    def set_text(self, text, colors, font):
        text_color, bg_color = colors
        self.text = font.render(text, True, pygame.Color(text_color))
        self.text_size = self.text.get_size()
        self.surface = pygame.Surface(self.text_size)
        self.surface.fill(bg_color)
        self.surface.blit(self.text_size, (0, 0))
        self.rect = pygame.Rect(self.middle_x, self.y, *self.text_size)


class ResizingText:
    def __init__(self, text, max_x, colors, font):
        text_color, bg_color = colors
        space = font.size(' ')[0]
        words = [sentence.split(' ') for sentence in text.splitlines()]
        line_x, surface_y = 0, 0
        for line in words:
            for word in line:
                word_size_x, word_size_y = font.render(word, True, text_color).get_size()
                if line_x + word_size_x > max_x:
                    surface_y += word_size_y
                    line_x = 0
                line_x += word_size_x + space
            line_x = 0
            surface_y += word_size_y

        self.new_surface = pygame.Surface(max_x, surface_y)
        
        for line in words:
            for word in line:
            
