import pygame
from new_version.player import Player
from new_version.enemy import Enemy

pygame.init()
BG = pygame.transform.scale(pygame.image.load('images/background.jpg'), (1280, 960))
PLACE_HOLDER_ENEMY = Enemy(placeholder=True)  # Used to run enemy functions


class LevelController:
    def __init__(self, display_dimensions):
        self._display_x, self._display_y = display_dimensions
        self._player = Player((int((self._display_x / 2) // 1), self._display_y - 200))
    
    @staticmethod
    def load_level_one():
        PLACE_HOLDER_ENEMY.generate_enemies(1)
    
    def update_game(self):
        for enemy_list in PLACE_HOLDER_ENEMY.return_enemies():
            for enemy in enemy_list:
                enemy.fire_bullet_check()
        
        for bullet in PLACE_HOLDER_ENEMY.return_bullets():
            if bullet.collision_check(self._player.return_rect()):
                PLACE_HOLDER_ENEMY.delete_bullet(bullet)
        
        to_remove_enemy = []
        to_remove_player_bullets = []
        for bullet in self._player.return_bullets():
            for enemy_list in range(len(PLACE_HOLDER_ENEMY.return_enemies())):
                for enemy in range(len(PLACE_HOLDER_ENEMY.return_enemies()[enemy_list])):
                    if bullet.collision_check(PLACE_HOLDER_ENEMY.return_enemies()[enemy_list][enemy].return_rect()):
                        to_remove_enemy.append((enemy_list, PLACE_HOLDER_ENEMY.return_enemies()[enemy_list][enemy]))
                        to_remove_player_bullets.append(bullet)
        
        for bullet in to_remove_player_bullets:
            self._player.delete_bullet(bullet)
        
        for enemy in to_remove_enemy:
            PLACE_HOLDER_ENEMY.delete_enemy(enemy[0], enemy[1])
            to_remove_enemy.remove(enemy)
        
        to_remove_enemy_list = []
        for enemy_list in PLACE_HOLDER_ENEMY.return_enemies():
            if enemy_list == []:
                to_remove_enemy_list.append(enemy_list)
        
        for enemy_list in to_remove_enemy_list:
            PLACE_HOLDER_ENEMY.delete_enemy_list(enemy_list)
        
        if PLACE_HOLDER_ENEMY.return_enemies():
            PLACE_HOLDER_ENEMY.update_enemies()
        PLACE_HOLDER_ENEMY.update_bullets()
        self._player.update_bullet()
        self._player.update_player()
    
    def move_player(self, direction):
        self._player.move_player(direction)
    
    def player_fire(self):
        self._player.fire_bullet()
    
    def return_screen(self):
        enemy_lists = PLACE_HOLDER_ENEMY.return_enemies()
        screen = pygame.Surface(BG.get_size())
        screen.blit(BG, (0, 0))
        for enemies in enemy_lists:
            for enemy in enemies:
                screen.blit(enemy.return_sprite(), (*enemy.return_pos(),))
        
        enemy_bullets = PLACE_HOLDER_ENEMY.return_bullets()
        for bullet in enemy_bullets:
            screen.blit(bullet.return_sprite(), (*bullet.return_pos(),))
        
        for bullet in self._player.return_bullets():
            screen.blit(bullet.return_sprite(), (*bullet.return_pos(),))
        
        screen.blit(self._player.return_sprite(), (*self._player.return_pos(),))
        
        return screen
