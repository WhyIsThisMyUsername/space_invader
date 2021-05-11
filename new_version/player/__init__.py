import pygame
from new_version.player_bullet import PlayerBullet

pygame.init()


class Player:
    _bullet_list = []
    
    def __init__(self, pos):
        self._player_x, self._player_y = pos
        self._lives = 3
        self._firing_speed = 40
        self._bullet_cooldown = 0
        
        self._sprite = pygame.image.load('images/player.png')
        self._sprite = pygame.transform.scale(self._sprite, (70, 70))
        
        self._rect = pygame.Rect(self._player_x, self._player_y, 70, 70)
    
    def move_player(self, direction):
        if direction == 'left' and not self._player_x < 70:
            self._player_x -= 10
            self._rect = self._rect.move(-20, 0)
        elif direction == 'right' and not self._player_x > 1210:
            self._player_x += 10
            self._rect = self._rect.move(20, 0)
    
    def fire_bullet(self):
        if self._bullet_cooldown <= 0:
            self._bullet_list.append(PlayerBullet((self._player_x + 15, self._player_y), 1))
            self._bullet_cooldown = self._firing_speed
    
    def update_bullet(self):
        for bullet in self._bullet_list:
            bullet.update_bullet()
    
    @staticmethod
    def return_bullets():
        return Player._bullet_list
    
    def return_sprite(self):
        return self._sprite
    
    def return_pos(self):
        return self._player_x, self._player_y
    
    @staticmethod
    def delete_bullet(bullet):
        Player._bullet_list.remove(bullet)
    
    def return_rect(self):
        return self._rect
    
    def update_player(self):
        self._bullet_cooldown -= 1
