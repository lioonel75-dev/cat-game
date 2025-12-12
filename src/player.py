import pygame
from src.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_group):
        super().__init__()
        self.bullet_group = bullet_group
        
        # Load sprites
        self.sprites = {
            'idle': pygame.image.load('assets/sprites/player_idle.png'),
            'run1': pygame.image.load('assets/sprites/player_run1.png'),
            'run2': pygame.image.load('assets/sprites/player_run2.png'),
            'jump': pygame.image.load('assets/sprites/player_jump.png')
        }
        
        self.image = self.sprites['idle']
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Movement
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.jump_power = -15
        self.gravity = 0.8
        self.on_ground = False
        self.facing_right = True
        
        # Double jump
        self.jump_count = 0
        self.max_jumps = 2  # 2 = double jump
        
        # Animation
        self.animation_counter = 0
        self.current_sprite = 'idle'
        
        # Combat
        self.health = 100
        self.shoot_cooldown = 0
        self.shoot_delay = 10
        self.alive = True
        
    def update(self, platforms):
        if not self.alive:
            return
            
        # Apply gravity
        self.vel_y += self.gravity
        if self.vel_y > 20:
            self.vel_y = 20
        
        # Movement
        keys = pygame.key.get_pressed()
        self.vel_x = 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x = -self.speed
            self.facing_right = False
            self.current_sprite = 'run'
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x = self.speed
            self.facing_right = True
            self.current_sprite = 'run'
        else:
            self.current_sprite = 'idle'
        
        # Double Jump
        # Detect jump key press (not just held)
        jump_pressed = keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]
        
        if jump_pressed and not hasattr(self, 'jump_key_held'):
            self.jump_key_held = False
        
        if jump_pressed and not self.jump_key_held:
            if self.jump_count < self.max_jumps:
                self.vel_y = self.jump_power
                self.jump_count += 1
                self.jump_key_held = True
        elif not jump_pressed:
            self.jump_key_held = False
        
        # Shoot
        if keys[pygame.K_x] or keys[pygame.K_LCTRL]:
            self.shoot()
        
        # Update position
        self.rect.x += self.vel_x
        self.check_collision_x(platforms)
        
        self.rect.y += self.vel_y
        self.on_ground = False
        self.check_collision_y(platforms)
        
        # Update animation
        self.update_animation()
        
        # Update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    
    def check_collision_x(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_x > 0:  # Moving right
                    self.rect.right = platform.rect.left
                elif self.vel_x < 0:  # Moving left
                    self.rect.left = platform.rect.right
    
    def check_collision_y(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:  # Falling
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                    self.jump_count = 0  # Reset jump count saat mendarat
                elif self.vel_y < 0:  # Jumping
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0
    
    def update_animation(self):
        self.animation_counter += 1
        
        if not self.on_ground:
            self.image = self.sprites['jump']
        elif self.current_sprite == 'run':
            if self.animation_counter % 10 < 5:
                self.image = self.sprites['run1']
            else:
                self.image = self.sprites['run2']
        else:
            self.image = self.sprites['idle']
        
        # Flip sprite based on direction
        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
    
    def shoot(self):
        if self.shoot_cooldown == 0:
            bullet_x = self.rect.right if self.facing_right else self.rect.left
            bullet_y = self.rect.centery
            direction = 1 if self.facing_right else -1
            
            bullet = Bullet(bullet_x, bullet_y, direction, 'player')
            self.bullet_group.add(bullet)
            self.shoot_cooldown = self.shoot_delay
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False
    
    def draw_health_bar(self, screen):
        bar_width = 100
        bar_height = 10
        bar_x = 10
        bar_y = 10
        
        # Background bar
        pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        # Health bar
        health_width = int((self.health / 100) * bar_width)
        pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, health_width, bar_height))
        # Border
        pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, bar_width, bar_height), 2)
