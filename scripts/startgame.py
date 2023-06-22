import pygame

from scripts.game import Game
from scripts.menu import Menu

from scripts.settings import *

class StartGame:
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('FLAPPY LULA')
        
        self.loop = True
        self.fps = pygame.time.Clock()
        self.scene = 'menu'
        self.current_scene = Menu()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            self.current_scene.events(event)
    
    def run(self):
        while self.loop:
            self.fps.tick(30)
            
            if not self.current_scene.active and self.scene == 'menu':
                self.scene = 'game'
                self.current_scene = Game()
            elif not self.current_scene.active and self.scene == 'game':
                self.scene = 'menu'
                self.current_scene = Menu()
            
            self.events()

            self.display.fill(BLACK)
            
            self.current_scene.draw()
            self.current_scene.update()
            
            pygame.display.flip()