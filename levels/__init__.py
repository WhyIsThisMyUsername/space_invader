import pygame
from players import Player
from enemies import Enemy
from game_components import Bullet

pygame.init()


class LevelController:
    def __init__(self, screen, display_x, display_y):
        self.player_bullets = []
        self.enemy_bullets = []
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
        self.animation_speed = 20
        self.animation_progress = 0
        self.animation_type = 0
        self.lives = 3
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
    
    def player_fire_bullet(self):
        self.player_bullets.append(Bullet(self.player.x + 15, self.player.y - 10, 'white'))
    
    def enemy_fire_bullet(self, x, y):
        self.enemy_bullets.append(Bullet(x, y, 'red'))
    
    def blit_screen(self):
        for i in self.enemy_bullets:
            if pygame.sprite.collide_rect(i, self.player):
                print('COLLIDE')

        enemy_count = 0
        for x in self.to_blit_enemy_lists:
            for y in x:
                enemy_count += 1
        if 20 <= enemy_count < 24:
            self.animation_speed = 18
            Enemy.bullet_chance = 18
        elif 15 <= enemy_count < 20:
            self.animation_speed = 15
            Enemy.bullet_chance = 15
        elif 10 <= enemy_count < 15:
            self.animation_speed = 11
            Enemy.bullet_chance = 11
        elif 5 <= enemy_count < 10:
            self.animation_speed = 5
            Enemy.bullet_chance = 5
        elif 0 <= enemy_count < 5:
            self.animation_speed = 2
            Enemy.bullet_chance = 2

        for i in self.player_bullets:
            i.bullet_progress += 1
            if i.bullet_progress >= i.bullet_speed:
                i.y -= 5
                i.rect = i.rect.move(0, -5)
                i.bullet_progress = 0
            if i.y < 0:
                self.player_bullets.remove(i)
        
        for x in range(len(self.to_blit_enemy_lists)):
            for y in range(len(self.to_blit_enemy_lists[x])):
                if self.to_blit_enemy_lists[x][y].fire_bullet_check():
                    print(True)
                    self.enemy_fire_bullet(self.to_blit_enemy_lists[x][y].x, self.to_blit_enemy_lists[x][y].y)
        
        for i in self.enemy_bullets:
            i.bullet_progress += 1
            if i.bullet_progress >= i.bullet_speed:
                i.y += 5
                i.rect = i.rect.move(0, +5)
                i.bullet_progress = 0
            if i.y > 960:
                self.enemy_bullets.remove(i)


        
        print(self.lives)

    
        self.to_remove = []
        for i in self.player_bullets:
            for x in range(len(self.to_blit_enemy_lists)):
                for y in range(len(self.to_blit_enemy_lists[x])):
                    if pygame.sprite.collide_rect(i, self.to_blit_enemy_lists[x][y]):
                        self.to_remove.append((i, x, y))
        
        for i, x, y in self.to_remove:
            self.player_bullets.remove(i)
            del self.to_blit_enemy_lists[x][y]
        
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
                        self.to_blit_enemy_lists[x][y].rect = self.to_blit_enemy_lists[x][y].rect.move(-7, 0)
                    else:
                        self.to_blit_enemy_lists[x][y].x += 7
                        self.to_blit_enemy_lists[x][y].rect = self.to_blit_enemy_lists[x][y].rect.move(7, 0)
        
        self.to_remove = []
        for i in range(len(self.to_blit_enemy_lists)):
            if not self.to_blit_enemy_lists[i]:
                self.to_remove.append(i)
        for i in self.to_remove:
            del self.to_blit_enemy_lists[i]

        for i in self.enemy_bullets:
            if pygame.sprite.collide_rect(i, self.player):
                self.lives -= 1
                self.enemy_bullets.remove(i)
        
        if self.to_blit_enemy_lists != []:
            left_row = self.to_blit_enemy_lists[0][0].x
            right_row = self.to_blit_enemy_lists[-1][0].x
        
            if self.going_left:
                if left_row < 140:
                    for x in range(len(self.to_blit_enemy_lists)):
                        for y in range(len(self.to_blit_enemy_lists[x])):
                            self.to_blit_enemy_lists[x][y].y += 75
                            self.to_blit_enemy_lists[x][y].rect = self.to_blit_enemy_lists[x][y].rect.move(0, 75)
                    self.going_left = False
            
            else:
                if right_row > 1100:
                    for x in range(len(self.to_blit_enemy_lists)):
                        for y in range(len(self.to_blit_enemy_lists[x])):
                            self.to_blit_enemy_lists[x][y].y += 75
                            self.to_blit_enemy_lists[x][y].rect = self.to_blit_enemy_lists[x][y].rect.move(0, 75)
                    self.going_left = True
        
        for x in self.to_blit_enemy_lists:
            for y in x:
                self.screen.blit(y.sprites[self.animation_type], (y.x, y.y))
        
        for i in self.player_bullets:
            self.screen.blit(i.sprite, (i.x, i.y))
        
        for i in self.enemy_bullets:
            self.screen.blit(i.sprite, (i.x, i.y))
        
        self.screen.blit(self.player.sprite, (self.player.x, self.player.y))
