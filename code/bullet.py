import pygame
BULLET_SPRITE = pygame.Surface((10,10)); BULLET_SPRITE.fill((255,255,255))


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        super().__init__()
        self.image = BULLET_SPRITE
        self.rect = self.image.get_rect(center=(x,y))
        self.direction = direction
        self.speed = 10


def update(self):
    if self.direction=="up": self.rect.y-=self.speed
    elif self.direction=="down": self.rect.y+=self.speed
    elif self.direction=="left": self.rect.x-=self.speed
    else: self.rect.x+=self.speed


    if self.rect.right<0 or self.rect.left>800 or self.rect.bottom<0 or self.rect.top>600:
    self.kill()