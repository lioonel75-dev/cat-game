import pygame
import random
from src.bullet import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_group):
        super().__init__()
        self.bullet_group = bullet_group
        
        # Load sprites
        self.sprites = {
            'idle': pygame.image.load('assets/sprites/enemy_idle.png'),
            'walk': pygame.image.load('assets/sprites/enemy_walk.png')
        }
        
        self.image = self.sprites['idle']
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Movement
        self.vel_x = -2
        self.vel_y = 0
        self.gravity = 0.8
        self.on_ground = False
        self.facing_right = False
        
        # Animation
        self.animation_counter = 0
        
        # Combat
        self.health = 50
        self.shoot_cooldown = 0
        self.shoot_delay = random.randint(60, 120)
        self.alive = True
        
        # AI
        self.ai_state = 'patrol'  # patrol, chase, shoot
        self.detection_range = 300
        self.shoot_range = 250
        
    def update(self, platforms, player):
        if not self.alive:
            return
        
        # Apply gravity
        self.vel_y += self.gravity
        if self.vel_y > 20:
            self.vel_y = 20
        
        # AI behavior
        self.ai_behavior(player)
        
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
    
    def ai_behavior(self, player):
        if not player.alive:
            self.ai_state = 'patrol'
            return
        
        distance = abs(player.rect.centerx - self.rect.centerx)
        
        if distance < self.shoot_range:
            self.ai_state = 'shoot'
            self.vel_x = 0
            if self.shoot_cooldown == 0:
                self.shoot(player)
        elif distance < self.detection_range:
            self.ai_state = 'chase'
            if player.rect.centerx < self.rect.centerx:
                self.vel_x = -2
                self.facing_right = False
            else:
                self.vel_x = 2
                self.facing_right = True
        else:
            self.ai_state = 'patrol'
            if self.vel_x == 0:
                self.vel_x = -2
                self.facing_right = False
    
    def check_collision_x(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_x > 0:
                    self.rect.right = platform.rect.left
                    self.vel_x = -2
                    self.facing_right = False
                elif self.vel_x < 0:
                    self.rect.left = platform.rect.right
                    self.vel_x = 2
                    self.facing_right = True
    
    def check_collision_y(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0
    
    def update_animation(self):
        self.animation_counter += 1
        
        if abs(self.vel_x) > 0:
            if self.animation_counter % 15 < 7:
                self.image = self.sprites['walk']
            else:
                self.image = self.sprites['idle']
        else:
            self.image = self.sprites['idle']
        
        # Flip sprite based on direction
        if self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
    
    def shoot(self, player):
        if self.shoot_cooldown == 0:
            bullet_x = self.rect.left if not self.facing_right else self.rect.right
            bullet_y = self.rect.centery
            direction = -1 if player.rect.centerx < self.rect.centerx else 1
            
            bullet = Bullet(bullet_x, bullet_y, direction, 'enemy')
            self.bullet_group.add(bullet)
            self.shoot_cooldown = self.shoot_delay
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.kill()
