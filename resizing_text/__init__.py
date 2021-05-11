# Imports
import pygame

# Initializes pygame
pygame.init()

# Creates class for Resizing Text: Text that automatically resizes based on the avaliable space
class ResizingText:
    # Sets position and runs the set text function
    def __init__(self, text, pos, max_x, colors, font):
        self.set_text(text, max_x, colors, font)
        self._x, self._y = pos
    
    def set_text(self, text, max_x, colors, font):
        # Sets colors and width of a single space
        text_color, bg_color = colors
        space = font.size(' ')[0]
        
        # Separates words and resets positioning for text
        words = [sentence.split(' ') for sentence in text.splitlines()]
        line_x, surface_y = 0, 0
        
        # Calculates overall size of the text
        for line in words:
            for word in line:
                word_size_x, word_size_y = font.render(word, True, text_color).get_size()
                if line_x + word_size_x > max_x:
                    surface_y += word_size_y
                    line_x = 0
                line_x += word_size_x + space
            line_x = 0
            surface_y += word_size_y
        
        # Creates a surface according to the size of the text
        self._new_surface = pygame.Surface((max_x, surface_y))
        self._new_surface.fill((15, 15, 15))
        
        # Creates text and blits it to the surface
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
    
    # Returns the surface
    def return_text(self):
        return self._new_surface
    
    # Returns the position
    def return_pos(self):
        return self._x, self._y
