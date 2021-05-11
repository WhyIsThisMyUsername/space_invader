# Imports
import pygame
from player_bullet import PlayerBullet

# Initializes pygame
pygame.init()

# Creates player class
class Player:
    # List of all bullets fired by the player
    _bullet_list = []
    
    # Generates positioning, lives, firing speed, cooldown, sprites and hitbox
    def __init__(self, pos):
        self._player_x, self._player_y = pos
        self._lives = 3
        self._firing_speed = 40
        self._bullet_cooldown = 0
        
        self._sprite = pygame.image.load('images/player.png')
        self._sprite = pygame.transform.scale(self._sprite, (70, 70))
        
        self._rect = pygame.Rect(self._player_x, self._player_y, 70, 70)
    
    # Moves player according to direction if it's not out of bounds
    def move_player(self, direction):
        if direction == 'left' and not self._player_x < 70:
            self._player_x -= 10
            self._rect = self._rect.move(-10, 0)
        elif direction == 'right' and not self._player_x > 1210:
            self._player_x += 10
            self._rect = self._rect.move(10, 0)
    
    # Fires a bullet if possible
    def fire_bullet(self):
        if self._bullet_cooldown <= 0:
            self._bullet_list.append(PlayerBullet((self._player_x + 15, self._player_y), 1))
            self._bullet_cooldown = self._firing_speed
    
    # Updates all bullets fired by the player
    def update_bullet(self):
        for bullet in self._bullet_list:
            bullet.update_bullet()
    
    # Returns list of player-fired bullets
    @staticmethod
    def return_bullets():
        return Player._bullet_list
    
    # Returns player sprite for blitting
    def return_sprite(self):
        return self._sprite
    
    # Returns player position for blitting
    def return_pos(self):
        return self._player_x, self._player_y
    
    # Deletes bullet
    @staticmethod
    def delete_bullet(bullet):
        Player._bullet_list.remove(bullet)
    
    # Returns hitbox
    def return_rect(self):
        return self._rect
    
    # Updates all player related values (granted, its not much)
    def update_player(self):
        self._bullet_cooldown -= 1
    
    # Removes a life
    def remove_life(self):
        self._lives -= 1
    
    # Returns the number of lives
    def return_lives(self):
        return self._lives
    
    # Sets number of lives
    def set_lives(self, lives):
        self._lives = lives
    
    # Resets player positioning and bullets
    def reset(self):
        self._player_x, self._player_y = int(1280 / 2 // 1), 960 - 200
        Player._bullet_list = []
