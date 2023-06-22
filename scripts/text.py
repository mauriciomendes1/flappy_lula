import pygame

class Text:
    def __init__(self, text, color, size, pos):
        
        self.size = size
        self.text = text
        self.color = color
        self.pos = pos
        self.display = pygame.display.get_surface()
        
        self.fade = 255
        self.font = pygame.font.Font('assets/font/font.ttf', self.size)
        self.render = self.font.render(self.text, True, self.color).convert_alpha()
        
        
    def draw(self):
        self.display.blit(self.render, self.pos)
    
    def draw_fade(self):
        if self.fade > 0:
            self.fade -= 5
        if self.fade <= 0:
            self.fade = 255
        self.render.set_alpha(self.fade)
        self.display.blit(self.render, self.pos)
    
    def update(self):
        self.draw()