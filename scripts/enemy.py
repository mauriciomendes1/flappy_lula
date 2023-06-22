import pygame

from scripts.obj import Obj

class Enemy(Obj):
    def __init__(self, img, pos, *groups) -> None:
        super().__init__(img, pos, *groups)
        
    def move(self):
        self.rect.x -= 5
        if self.rect.x < -200:
            self.kill()
            
    def update(self) -> None:
        self.move()