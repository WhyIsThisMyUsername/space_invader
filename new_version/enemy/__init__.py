import pygame
import random
from new_version.enemy_bullet import EnemyBullet

pygame.init()
DISPLAY_X = 1280
IMAGE_SET_ONE = [pygame.image.load('images/enemy_1-1.png'), pygame.image.load('images/enemy_1-2.png')]
IMAGE_SET_TWO = [pygame.image.load('images/enemy_2-1.png'), pygame.image.load('images/enemy_2-2.png')]
IMAGE_SET_THREE = [pygame.image.load('images/enemy_3-1.png'), pygame.image.load('images/enemy_3-2.png')]
ALL_SPRITES = [IMAGE_SET_ONE, IMAGE_SET_TWO, IMAGE_SET_THREE]

for list_id in range(len(ALL_SPRITES)):
    for image_id in range(len(ALL_SPRITES[list_id])):
        ALL_SPRITES[list_id][image_id] = pygame.transform.scale(ALL_SPRITES[list_id][image_id], (70, 70))


class Enemy:
    _bullet_chance = 30
    _bullet_list = []
    _bullet_delay = 60
    _enemy_list = []
    _animation_speed = 30
    _animation_charge = 0
    _animation_type = 0
    _going_left = True
    
    def __init__(self, pos=None, images=None, placeholder=False):
        if not placeholder:
            self._bullet_charge = 0
            self._sprites = images
            self._enemy_x, self._enemy_y = pos
            self._rect = pygame.Rect(self._enemy_x, self._enemy_y, *self._sprites[0].get_size())
    
    def fire_bullet_check(self):
        if self._bullet_charge < Enemy._bullet_delay:
            self._bullet_charge += 1
        if self._bullet_charge >= Enemy._bullet_delay:
            self._bullet_charge = 0
            if not random.randint(0, Enemy._bullet_chance):
                self._fire_bullet()
    
    def _fire_bullet(self):
        Enemy._bullet_list.append(EnemyBullet((self._enemy_x + 35, self._enemy_y + 70), 1))
    
    @staticmethod
    def update_bullets():
        for bullet in Enemy._bullet_list:
            bullet.update_bullet()
    
    @staticmethod
    def update_enemies():
        Enemy._animation_charge += 1
        if Enemy._animation_charge >= Enemy._animation_speed:
            Enemy._animation_charge = 0
            if Enemy._animation_type == 0:
                Enemy._animation_type = 1
            else:
                Enemy._animation_type = 0
        
        if Enemy._animation_charge == 0:
            if Enemy._going_left:
                Enemy.move_enemies('left')
            else:
                Enemy.move_enemies('right')
    
        total_enemies = 0
        for enemy_list in Enemy._enemy_list:
            for enemy in enemy_list:
                total_enemies += 1
        
        if 20 <= total_enemies < 24:
            Enemy._animation_speed = 18
            Enemy._bullet_chance = 18
        elif 15 <= total_enemies < 20:
            Enemy._animation_speed = 15
            Enemy._bullet_chance = 15
        elif 10 <= total_enemies < 15:
            Enemy._animation_speed = 11
            Enemy._bullet_chance = 11
        elif 5 <= total_enemies < 10:
            Enemy._animation_speed = 5
            Enemy._bullet_chance = 5
        elif 0 <= total_enemies < 5:
            Enemy._animation_speed = 2
            Enemy._bullet_chance = 2
    
    @staticmethod
    def move_enemies(direction):
        if direction == 'left':
            if Enemy._enemy_list[0][0].return_pos()[0] < 70:
                for enemy_list in Enemy.return_enemies():
                    for enemy in enemy_list:
                        enemy.move_enemy('left', down=True)
            else:
                for enemy_list in Enemy.return_enemies():
                    for enemy in enemy_list:
                        enemy.move_enemy('left')
        else:
            if Enemy._enemy_list[-1][0].return_pos()[0] > 1210 - 70:
                for enemy_list in Enemy.return_enemies():
                    for enemy in enemy_list:
                        enemy.move_enemy('right', down=True)
            else:
                for enemy_list in Enemy.return_enemies():
                    for enemy in enemy_list:
                        enemy.move_enemy('right')
    
    def move_enemy(self, direction, down=False):
        if direction == 'left':
            if down:
                self._enemy_y += 75
                self._rect = self._rect.move(0, 75)
                Enemy._going_left = False
            else:
                self._enemy_x -= 7
                self._rect = self._rect.move(-7, 0)
        
        else:
            if down:
                self._enemy_y += 75
                self._rect = self._rect.move(0, 75)
                Enemy._going_left = True
            else:
                self._enemy_x += 7
                self._rect = self._rect.move(7, 0)
    
    def return_pos(self):
        return self._enemy_x, self._enemy_y
    
    @staticmethod
    def generate_enemies(level):
        if level == 1:
            working_size = (240, DISPLAY_X - 240 - 70)  # 240 gives enough room at the sides for enemies to move,
            # 70 is roughly the size of an enemy
            current_x = working_size[0]
            while current_x <= working_size[1]:
                Enemy._enemy_list.append([])
                Enemy._enemy_list[-1].append(Enemy((current_x + 15, 100), IMAGE_SET_ONE))
                Enemy._enemy_list[-1].append(Enemy((current_x + 5, 170), IMAGE_SET_TWO))
                Enemy._enemy_list[-1].append(Enemy((current_x, 250), IMAGE_SET_THREE))
                current_x += 100
    
    @staticmethod
    def return_enemies():
        return Enemy._enemy_list
    
    def return_sprite(self):
        if Enemy._animation_type == 0:
            return self._sprites[0]
        else:
            return self._sprites[1]
    
    def return_rect(self):
        return self._rect
    
    @staticmethod
    def return_bullets():
        return Enemy._bullet_list
    
    @staticmethod
    def delete_bullet(bullet):
        Enemy._bullet_list.remove(bullet)
    
    @staticmethod
    def delete_enemy(enemy_list, enemy):
        Enemy._enemy_list[enemy_list].remove(enemy)
    
    @staticmethod
    def delete_enemy_list(enemy_list):
        Enemy._enemy_list.remove(enemy_list)