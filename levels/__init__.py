import pygame
from players import Player
from enemies import Enemy

pygame.init()


class LevelController:
    def __init__(self, screen, display_x, display_y):
        self.bullets = []
        self.animation_progress = 0
        self.animation_speed = 30
        self.animation_type = 0
        self.to_blit_enemy_lists = []
        self.to_blit_bullets = []
        self.screen = screen
        self.display_x, self.display_y = display_x, display_y
        self.player = Player(display_x / 2, display_y - 100)
        self.enemy_1 = [pygame.image.load('images/enemy_1-1.png'), pygame.image.load('images/enemy_1-2.png')]
        self.enemy_2 = [pygame.image.load('images/enemy_2-1.png'), pygame.image.load('images/enemy_2-2.png')]
        self.enemy_3 = [pygame.image.load('images/enemy_3-1.png'), pygame.image.load('images/enemy_3-2.png')]
        self.enemy_sprites = [self.enemy_1, self.enemy_2, self.enemy_3]
        
        for x in range(len(self.enemy_sprites)):
            for y in range(len(self.enemy_sprites[x])):
                self.enemy_sprites[x][y] = pygame.transform.scale(self.enemy_sprites[x][y], (70, 70))
    
    def load_level_one(self):
        self.going_left = True
        self.animation_speed = 10
        self.animation_progress = 0
        self.animation_type = 0
        self.to_blit_enemy_lists = []
        self.to_blit_bullets = []
        working_size = (240, self.display_x - 240 - 100)
        current_x = working_size[0]
        while current_x <= working_size[1]:
            self.to_blit_enemy_lists.append([])
            self.to_blit_enemy_lists[-1].append(Enemy(self.enemy_1, current_x + 15, 100))
            self.to_blit_enemy_lists[-1].append(Enemy(self.enemy_2, current_x + 5, 175))
            self.to_blit_enemy_lists[-1].append(Enemy(self.enemy_3, current_x, 250))
            current_x += 100
    
    def fire_bullet(self):
    
    
    def blit_screen(self):
        self.animation_progress += 1
        if self.animation_progress >= self.animation_speed:
            self.animation_progress = 0
            if self.animation_type == 0:
                self.animation_type = 1
            else:
                self.animation_type = 0
        
        if self.animation_progress == 0:
            for x in range(len(self.to_blit_enemy_lists)):
                for y in range(len(self.to_blit_enemy_lists[x])):
                    if self.going_left:
                        self.to_blit_enemy_lists[x][y].x -= 7
                    else:
                        self.to_blit_enemy_lists[x][y].x += 7

        for i in range(len(self.to_blit_enemy_lists)):
            if self.to_blit_enemy_lists[i] == []:
                del self.to_blit_enemy_lists[i]
        
        left_row = self.to_blit_enemy_lists[0][0].x
        right_row = self.to_blit_enemy_lists[-1][0].x
        
        if self.going_left:
            if left_row < 140:
                for x in range(len(self.to_blit_enemy_lists)):
                    for y in range(len(self.to_blit_enemy_lists[x])):
                        self.to_blit_enemy_lists[x][y].y += 75
                self.going_left = False
        
        else:
            if right_row > 1100:
                for x in range(len(self.to_blit_enemy_lists)):
                    for y in range(len(self.to_blit_enemy_lists[x])):
                        self.to_blit_enemy_lists[x][y].y += 75
                self.going_left = True

        for x in self.to_blit_enemy_lists:
            for y in x:
                self.screen.blit(y.sprites[self.animation_type], (y.x, y.y))
        
        for i in self.bullets:
        
        
        self.screen.blit(self.player.sprite, (self.player.x, self.player.y))
