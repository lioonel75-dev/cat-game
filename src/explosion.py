import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # Load explosion sprites
        self.sprites = []
        for i in range(4):
            sprite = pygame.image.load(f'assets/sprites/explosion_{i}.png')
            self.sprites.append(sprite)
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.animation_speed = 0.2
        self.animation_counter = 0
    
    def update(self):
        self.animation_counter += self.animation_speed
        
        if self.animation_counter >= 1:
            self.current_sprite += 1
            self.animation_counter = 0
            
            if self.current_sprite >= len(self.sprites):
                self.kill()
            else:
                self.image = self.sprites[self.current_sprite]
