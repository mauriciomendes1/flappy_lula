import pygame

from scripts.obj import Obj
from scripts.settings import *

class Player(Obj):
    def __init__(self, img, pos, *groups) -> None:
        super().__init__(img, pos, *groups)
        
        self.jump_sound = pygame.mixer.Sound('assets/sounds/jump.wav')
        self.jump_sound.set_volume(0.3)
        self.hit_sound = pygame.mixer.Sound('assets/sounds/hit.flac')
        self.cachaca_sound = pygame.mixer.Sound('assets/sounds/burp.mp3')
        
        self.gravity = 4
        self.speed = 1
        self.live = True
        self.tick = 0
        self.pts = 0
    
    def events(self, event):
        if self.live:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.jump_sound.play()
                    self.gravity -= 10
    
    def gravity_force(self):
        self.gravity += self.speed
        self.rect.y += self.gravity
        if self.gravity >= 10:
            self.gravity = 4
            
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= HEIGHT - 95:
            self.rect.y = HEIGHT - 95
                
    def collision_moro(self, group):
        
        collision = pygame.sprite.spritecollide(self, group, False, pygame.sprite.collide_mask)
        
        if collision:
            self.hit_sound.play()
            self.live = False
            
    def collision_cachaca(self, group):
        
        collision = pygame.sprite.spritecollide(self, group, True, pygame.sprite.collide_mask)
        if collision:
            self.cachaca_sound.play()
            self.pts += 1
    
    def draw(self):
        pass

    def update(self):
        pass