import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, platform_type='ground'):
        super().__init__()
        
        if platform_type == 'ground':
            # Load platform sprite and tile it
            tile = pygame.image.load('assets/sprites/platform.png')
            tile_width = tile.get_width()
            tile_height = tile.get_height()
            
            self.image = pygame.Surface((width, height))
            for i in range(0, width, tile_width):
                for j in range(0, height, tile_height):
                    self.image.blit(tile, (i, j))
        else:
            # Simple colored platform
            self.image = pygame.Surface((width, height))
            self.image.fill((100, 100, 100))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
