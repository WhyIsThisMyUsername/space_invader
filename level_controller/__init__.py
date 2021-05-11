# Imports
import pygame
from player import Player
from enemy import Enemy

# Initializing pygame and setting base variables
pygame.init()
BG = pygame.transform.scale(pygame.image.load('images/background.jpg'), (1280, 960))
PLACE_HOLDER_ENEMY = Enemy(placeholder=True)  # Used to run enemy functions
MEDIUM_BUTTON_FONT = pygame.font.SysFont('Corbel', 70)


class LevelController:
    # Sets display size, creates player, and sets game (for the actual game part) status
    def __init__(self, display_dimensions):
        self._display_x, self._display_y = display_dimensions
        self._player = Player((int((self._display_x / 2) // 1), self._display_y - 200))
        self._game_status = 'Ongoing'
    
    # Loads the first level, resets lives and player positions just in case
    def load_level_one(self):
        PLACE_HOLDER_ENEMY.generate_enemies(1)
        print('LOAD LEVEL 1')
        self._game_status = 'Level 1'
        self._player.set_lives(3)
        self._player.reset()
    
    # Updates all objects in the game as needed
    def update_game(self):
        # Checks each enemy to see if it will fire a bullet
        for enemy_list in PLACE_HOLDER_ENEMY.return_enemies():
            for enemy in enemy_list:
                enemy.fire_bullet_check()
        
        # Checks if enemy bullets colliding with player, deletes bullet and removes life if true
        for bullet in PLACE_HOLDER_ENEMY.return_bullets():
            if bullet.collision_check(self._player.return_rect()):
                PLACE_HOLDER_ENEMY.delete_bullet(bullet)
                self._player.remove_life()
        
        # Checks if player bullets colliding with enemies, if true sets enemy and bullet for deletion
        to_remove_enemy = []
        to_remove_player_bullets = []
        for bullet in self._player.return_bullets():
            for enemy_list in range(len(PLACE_HOLDER_ENEMY.return_enemies())):
                for enemy in range(len(PLACE_HOLDER_ENEMY.return_enemies()[enemy_list])):
                    if bullet.collision_check(PLACE_HOLDER_ENEMY.return_enemies()[enemy_list][enemy].return_rect()):
                        to_remove_enemy.append((enemy_list, PLACE_HOLDER_ENEMY.return_enemies()[enemy_list][enemy]))
                        to_remove_player_bullets.append(bullet)
        
        # Checks if enemy is at the bottom of the screen, ends game if so
        for enemy_list in range(len(PLACE_HOLDER_ENEMY.return_enemies())):
            for enemy in range(len(PLACE_HOLDER_ENEMY.return_enemies()[enemy_list])):
                if PLACE_HOLDER_ENEMY.return_enemies()[enemy_list][enemy].return_pos()[1] > self._display_y - 200:
                    self._game_status = 'Defeat'
        
        # Deletes bullets now to prevent bugs from deleting during above loop
        for bullet in to_remove_player_bullets:
            self._player.delete_bullet(bullet)
        
        # Deletes enemies now to prevent bugs from deleting during above loop (same reason again)
        for enemy in to_remove_enemy:
            PLACE_HOLDER_ENEMY.delete_enemy(enemy[0], enemy[1])
            to_remove_enemy.remove(enemy)
        
        # Clears empty enemy lists to prevent bugs from accessing empty lists
        to_remove_enemy_list = []
        for enemy_list in PLACE_HOLDER_ENEMY.return_enemies():
            if enemy_list == []:
                PLACE_HOLDER_ENEMY.delete_enemy_list(enemy_list)
        
        # Checks if enemies exist before updating, else game crashes from accessing nonexistent enemies
        if PLACE_HOLDER_ENEMY.return_enemies():
            PLACE_HOLDER_ENEMY.update_enemies()
        
        # Updates all bullets and the player
        PLACE_HOLDER_ENEMY.update_bullets()
        self._player.update_bullet()
        self._player.update_player()
        
        # Checks if player has won or lost
        if not PLACE_HOLDER_ENEMY.return_enemies() and self._game_status == 'Level 1':
            self._game_status = 'Victory'
        
        if self._player.return_lives() < 0:
            self._game_status = 'Defeat'
    
    # Moves player left or right
    def move_player(self, direction):
        self._player.move_player(direction)
    
    # Player attempts to fire bullet
    def player_fire(self):
        self._player.fire_bullet()
    
    # Returns the screen to the main program to be blit
    def return_screen(self):
        enemy_lists = PLACE_HOLDER_ENEMY.return_enemies()
        screen = pygame.Surface(BG.get_size())
        screen.blit(BG, (0, 0))
        
        # Blits all enemies
        for enemies in enemy_lists:
            for enemy in enemies:
                screen.blit(enemy.return_sprite(), (*enemy.return_pos(),))
        
        # Blits both enemy and player bullets
        enemy_bullets = PLACE_HOLDER_ENEMY.return_bullets()
        for bullet in enemy_bullets:
            screen.blit(bullet.return_sprite(), (*bullet.return_pos(),))
        
        for bullet in self._player.return_bullets():
            screen.blit(bullet.return_sprite(), (*bullet.return_pos(),))
        
        # Blits players and number of lives
        screen.blit(self._player.return_sprite(), (*self._player.return_pos(),))
        screen.blit(self._lives_text(), (100, 820))
        
        return screen
    
    # Creates and returns text to blit lives
    def _lives_text(self):
        text = MEDIUM_BUTTON_FONT.render('Lives: ' + str(self._player.return_lives()), True, pygame.Color('white'))
        bg = pygame.Surface(text.get_size())
        bg.fill((15, 15, 15))
        bg.blit(text, (0, 0))
        return bg
    
    # Returns status on if game is ongoing, won or lost
    def return_status(self):
        return self._game_status
