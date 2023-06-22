import pygame

class Scene:
    def __init__(self) -> None:
        self.all_sprites = pygame.sprite.Group()
        self.display = pygame.display.get_surface()
        self.active = True
        
    def events(self, event):
        pass
    
    def draw(self):
        self.all_sprites.draw(self.display)
    
    def update(self):
        pass