import pygame

pygame.init()


class ResizingText:
    def __init__(self, text, pos, max_x, colors, font):
        self.set_text(text, max_x, colors, font)
        self._x, self._y = pos
    
    def set_text(self, text, max_x, colors, font):
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
        
        self._new_surface = pygame.Surface((max_x, surface_y))
        
        line_x, line_y = 0, 0
        for line in words:
            for word in line:
                text_surface = font.render(word, True, text_color)
                background_surface = pygame.Surface(text_surface.get_size())
                background_surface.fill(bg_color)
                print(type(background_surface))
                background_surface.blit(text_surface, (0, 0))
                word_width, word_height = background_surface.get_size()
                if line_x + word_width > max_x:
                    line_x = 0
                    line_y += word_height
                self._new_surface.blit(background_surface, (line_x, line_y))
                line_x += word_width + space
            line_x = 0
            line_y += word_height
    
    def return_text(self):
        return self._new_surface
    
    def return_pos(self):
        return self._x, self._y
