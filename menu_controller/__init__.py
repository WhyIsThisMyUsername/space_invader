# Imports
import pygame
from button import Button
from resizing_text import ResizingText
from bouncing_button import BouncingButton
from text import Text

# Initializing pygame and creating constants
pygame.init()

LARGE_BUTTON_FONT = pygame.font.SysFont('Corbel', 140)
MEDIUM_BUTTON_FONT = pygame.font.SysFont('Corbel', 70)
TEXT_COLOR = 'white'
TEXT_BG_COLOR = (15, 15, 15)
TEXT_COLOR_COMBO = (TEXT_COLOR, TEXT_BG_COLOR)
BG = pygame.transform.scale(pygame.image.load('images/background.jpg'), (1280, 960))


class MenuController:
    # Creates initial menu surface, and resets all lists that are used to blit objects
    def __init__(self, size):
        self._surface = pygame.Surface(size)
        self._reset_blits()
    
    # Generates buttons for main menu
    def main_menu(self):
        self._reset_blits()
        self._to_blit_buttons.append(Button('Start', (640, 200), TEXT_COLOR_COMBO, LARGE_BUTTON_FONT))
        self._to_blit_buttons.append(Button('Controls', (640, 400), TEXT_COLOR_COMBO, LARGE_BUTTON_FONT))
        self._to_blit_buttons.append(Button('Bouncy', (640, 600), TEXT_COLOR_COMBO, LARGE_BUTTON_FONT))
    
    # Generates text and button for controls menu
    def controls_menu(self):
        self._reset_blits()
        controls_text = 'Move Left = Left arrow\nMove Right = Right arrow\nFire = Spacebar'
        self._to_blit_buttons.append(Button('Return', (1160, 860), TEXT_COLOR_COMBO, MEDIUM_BUTTON_FONT))
        self._to_blit_resizing_text.append(
            ResizingText(controls_text, (100, 100), 900, TEXT_COLOR_COMBO, MEDIUM_BUTTON_FONT))
    
    # Generates button for bouncing button menu
    def bouncing_button_menu(self):
        self._reset_blits()
        self._to_blit_bouncing_buttons.append(
            BouncingButton('BOUNCE', (640, 800), TEXT_COLOR_COMBO, MEDIUM_BUTTON_FONT))
    
    # Updates the bouncing button
    def bouncing_button_update(self):
        for bouncing_button in self._to_blit_bouncing_buttons:
            bouncing_button.change_coordinates()
    
    # Generates victory screen
    def victory_screen(self):
        self._reset_blits()
        self._to_blit_text.append(Text('VICTORY', (640, 300), TEXT_COLOR_COMBO, LARGE_BUTTON_FONT))
        self._to_blit_buttons.append(Button('Replay?', (640, 700), TEXT_COLOR_COMBO, MEDIUM_BUTTON_FONT))
    
    # Generates defeat screen
    def defeat_screen(self):
        self._reset_blits()
        self._to_blit_text.append(Text('DEFEAT', (640, 300), TEXT_COLOR_COMBO, LARGE_BUTTON_FONT))
        self._to_blit_buttons.append(Button('Replay?', (640, 700), TEXT_COLOR_COMBO, MEDIUM_BUTTON_FONT))
    
    # Resets all lists as anything in a list gets blit, so clearing it resets menus
    def _reset_blits(self):
        self._to_blit_buttons = []
        self._to_blit_resizing_text = []
        self._to_blit_bouncing_buttons = []
        self._to_blit_text = []
    
    # Returns all buttons in list
    def return_buttons(self):
        return self._to_blit_buttons
    
    # Return all bouncing buttons in list
    def return_bouncing_buttons(self):
        return self._to_blit_bouncing_buttons
    
    # Returns screen to be blit to the main menu
    def return_screen(self):
        self._surface.blit(BG, (0, 0))
        
        # For object in all lists, blit object
        for button in self._to_blit_buttons:
            self._surface.blit(button.return_text(), button.return_coords())
        
        for resized_text in self._to_blit_resizing_text:
            self._surface.blit(resized_text.return_text(), (*resized_text.return_pos(),))
        
        for bouncing_button in self._to_blit_bouncing_buttons:
            self._surface.blit(bouncing_button.return_button(), (*bouncing_button.return_coordinates(),))
        
        for text in self._to_blit_text:
            self._surface.blit(text.return_text(), (*text.return_pos(),))
        
        return self._surface
