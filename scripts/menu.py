import pygame

from scripts.scene import Scene
from scripts.obj import Obj
from scripts.text import Text
from scripts.settings import *

class Menu(Scene):
    def __init__(self) -> None:
        super().__init__()
        
        self.bg = Obj('assets/imgs/bg_menu.png', (0,0), self.all_sprites)
        self.title = Text('FLAPPY LULA', BLUE, 70, (150, 200))
        self.start = Text('press enter to start', BLUE, 30, (170, 400))
        self.developer = Text('Desenvolvido por Mauricio Mendes', BLUE, 20, (150, 450))
        self.menu_sound = pygame.mixer.music.load('assets/sounds/menu_sound.mp3')
        pygame.mixer.music.play(-1)
        self.active = True
        
    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False
                pygame.mixer.music.stop()
    
    def draw(self):
        return super().draw()
    
    def update(self):
        self.title.update()
        self.start.draw_fade()
        self.developer.update()
        
        return super().update()