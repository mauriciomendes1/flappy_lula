import pygame, random

from scripts.animatedbg import Animatedbg
from scripts.cachaca import Cachaca
from scripts.enemy import Enemy
from scripts.player import Player
from scripts.settings import *
from scripts.scene import Scene
from scripts.text import Text


class Game(Scene):
    def __init__(self) -> None:
        super().__init__()
        self.bg = Animatedbg('assets/imgs/background.jpg', (0,0), (WIDTH,0), 5, self.all_sprites)
        self.enemy_group = pygame.sprite.Group()
        self.cachaca_group = pygame.sprite.Group()
        
        self.player = Player('assets/imgs/lula.png', (30, 300), self.all_sprites)
        self.enemy = Enemy('assets/imgs/moro_final.png', (WIDTH, random.randrange(250, 390)), self.all_sprites, self.enemy_group)
        self.enemy2 = Enemy('assets/imgs/moro_final.png', (WIDTH, self.enemy.rect.y - 350), self.all_sprites, self.enemy_group )
        self.enemy2.image = pygame.transform.flip(self.enemy2.image, False, True)
        self.cachaca = Cachaca('assets/imgs/cachaca.png', (self.enemy.rect.x + 150, self.enemy.rect.y - 50), self.all_sprites, self.cachaca_group)
        
        self.bg_sound = pygame.mixer.music.load('assets/sounds/background_sound.mp3')
        pygame.mixer.music.play(-1)
        
        self.score = Text('Score: ' + str(self.player.pts), BLACK, 20, (30, 30))
        self.ticks = 0
    
    def events(self, event):
        self.player.events(event)
    
    def draw(self):
        
        return super().draw()
    
    def spawn_enemy(self):
        
        if self.ticks >= 60:
            enemy = Enemy('assets/imgs/moro_final.png', (WIDTH, random.randrange(250, 390)), self.all_sprites, self.enemy_group)
            cachaca = Cachaca('assets/imgs/cachaca.png', (enemy.rect.x + 150, enemy.rect.y - 50), self.all_sprites, self.cachaca_group)
            enemy2 = Enemy('assets/imgs/moro_final.png', (WIDTH, enemy.rect.y - 350), self.all_sprites, self.enemy_group )
            enemy2.image = pygame.transform.flip(enemy2.image, False, True)
            self.ticks = 0

    def update(self):
        self.player.gravity_force()
        if self.player.live:
            self.ticks += 1
            self.spawn_enemy()
            self.bg.animatedbg()
            self.enemy.move()
            self.enemy2.move()
            self.player.collision_moro(self.enemy_group)
            self.player.collision_cachaca(self.cachaca_group)
            self.player.update()
            self.cachaca.update()
            self.score.update()
            self.score = Text('Score: ' + str(self.player.pts), BLACK, 20, (30, 30))
            self.score.update()
            self.all_sprites.update()
        else:
            pygame.mixer.music.stop()
            self.score_text = Text('Score', BLACK, 50, (250, 100))
            self.score = Text(str(self.player.pts), BLACK, 50, (300, 200))
            self.restart = Text('press enter to restart', BLACK, 30, (200, 300))
            self.score_text.update()
            self.score.update()
            self.restart.update()
            key = pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                self.active = False
        return super().update()