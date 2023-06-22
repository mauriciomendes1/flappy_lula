import pygame

from scripts.obj import Obj

class Cachaca(Obj):
    def __init__(self, img, pos, *groups) -> None:
        super().__init__(img, pos, *groups)
        
    def move(self):
        self.rect.x -= 5
        
    def update(self) -> None:
        self.move()
        return super().update()