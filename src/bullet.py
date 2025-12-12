import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, bullet_type='player'):
        super().__init__()
        
        # Load sprite
        if bullet_type == 'player':
            self.image = pygame.image.load('assets/sprites/bullet_player.png')
            self.damage = 25
        else:
            self.image = pygame.image.load('assets/sprites/bullet_enemy.png')
            self.damage = 10
        
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
        self.speed = 10
        self.direction = direction
        self.bullet_type = bullet_type
    
    def update(self):
        self.rect.x += self.speed * self.direction
        
        # Remove bullet if off screen
        if self.rect.right < 0 or self.rect.left > 1200:
            self.kill()
