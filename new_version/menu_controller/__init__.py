import pygame
from new_version.button import Button
from new_version.resizing_text import ResizingText

pygame.init()

LARGE_BUTTON_FONT = pygame.font.SysFont('Corbel', 140)
MEDIUM_BUTTON_FONT = pygame.font.SysFont('Corbel', 70)
TEXT_COLOR = 'white'
TEXT_BG_COLOR = (15, 15, 15)
TEXT_COLOR_COMBO = (TEXT_COLOR, TEXT_BG_COLOR)
BG = pygame.transform.scale(pygame.image.load('images/background.jpg'), (1280, 960))

class MenuController:
    def __init__(self, size):
        self._surface = pygame.Surface(size)
        self._reset_blits()

    def main_menu(self):
        self._reset_blits()
        self._to_blit_buttons.append(Button('Start', (640, 200), TEXT_COLOR_COMBO, LARGE_BUTTON_FONT))
        self._to_blit_buttons.append(Button('Controls', (640, 400), TEXT_COLOR_COMBO, LARGE_BUTTON_FONT))
        self._to_blit_buttons.append(Button('Bouncy', (640, 600), TEXT_COLOR_COMBO, LARGE_BUTTON_FONT))

    def controls_menu(self):
        self._reset_blits()
        controls_text = 'insert\ncontrols\nhere'
        self._to_blit_buttons.append(Button('Return', (1160, 860), TEXT_COLOR_COMBO, MEDIUM_BUTTON_FONT))
        self._to_blit_resizing_text.append(ResizingText(controls_text, (100, 100), 570, TEXT_COLOR_COMBO, MEDIUM_BUTTON_FONT))

    def bouncing_button_menu(self):
        self._reset_blits()


    def bouncing_button_update(self):


    def _reset_blits(self):
        self._to_blit_buttons = []
        self._to_blit_resizing_text = []
        self._to_blit_bouncing_buttons = []

    def return_buttons(self):
        return self._to_blit_buttons

    def return_bouncing_buttons(self):
        return self._to_blit_bouncing_buttons

    def return_screen(self):
        self._surface.blit(BG, (0, 0))

        for button in self._to_blit_buttons:
            self._surface.blit(button.return_text(), (*button.return_coords(),))

        for resized_text in self._to_blit_resizing_text:
            self._surface.blit(resized_text.return_text(), *resized_text.return_pos())

        for bouncing_button in self._to_blit_bouncing_buttons:
            pass

        return self._surface
