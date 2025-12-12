import pygame

class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # Create flag/goal sprite
        self.image = pygame.Surface((60, 80), pygame.SRCALPHA)
        
        # Tiang
        pygame.draw.rect(self.image, (100, 100, 100), (25, 0, 10, 80))
        
        # Bendera
        points = [(35, 10), (55, 20), (35, 30)]
        pygame.draw.polygon(self.image, (255, 215, 0), points)
        
        # Text "GOAL"
        font = pygame.font.Font(None, 20)
        text = font.render("GOAL", True, (255, 255, 255))
        self.image.blit(text, (5, 35))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Animation
        self.animation_counter = 0
        self.original_y = y
    
    def update(self):
        # Floating animation
        self.animation_counter += 0.1
        self.rect.y = self.original_y + int(pygame.math.Vector2(0, 10).rotate(self.animation_counter * 180 / 3.14159).y)
