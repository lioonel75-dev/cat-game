import pygame, random
ENEMY_SPRITE = pygame.Surface((40,40)); ENEMY_SPRITE.fill((200,50,50))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed, move_type):
        super().__init__()
        self.image = ENEMY_SPRITE
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100,700)
        self.rect.y = random.randint(100,500)
        self.speed = speed
        self.move_type = move_type
        self.direction = 1


    def update(self):
        if self.move_type == "vertical":
            self.rect.y += self.speed*self.direction
            if self.rect.top<=0 or self.rect.bottom>=600:
                self.direction*=-1
        else:
            self.rect.x += self.speed*self.direction
            if self.rect.left<=0 or self.rect.right>=800:
                self.direction*=-1