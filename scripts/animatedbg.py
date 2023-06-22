import pygame

from scripts.obj import Obj
from scripts.settings import *

class Animatedbg:
    def __init__(self, img, pos1, pos2, speed, group) -> None:
        self.bg = Obj(img, pos1, group)
        self.bg2 = Obj(img, pos2, group)
        
        self.speed = speed
        
    def animatedbg(self):
        self.bg.rect.x -= self.speed
        self.bg2.rect.x -= self.speed
        
        if self.bg.rect.x <= -WIDTH:
            self.bg.rect.x = WIDTH
        if self.bg2.rect.x <= -WIDTH:
            self.bg2.rect.x = WIDTH