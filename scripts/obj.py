import pygame

class Obj(pygame.sprite.Sprite):
    def __init__(self, img, pos, *groups) -> None:
        super().__init__(*groups)
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        