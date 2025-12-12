import pygame
import sys
from src.player import Player
from src.enemy import Enemy
from src.platform import Platform
from src.explosion import Explosion
from src.goal import Goal

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
LEVEL_HEIGHT = 2400  # Level lebih tinggi untuk vertical platforming
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Cat Climber - Climb to the Top!")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Game states
        self.state = "menu"  # menu, playing, game_over, victory
        self.game_over = False
        self.victory = False
        
        # Load background
        try:
            self.background = pygame.image.load('assets/sprites/background.png')
            self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, LEVEL_HEIGHT))
        except:
            self.background = None
        
        # Camera offset
        self.camera_y = 0
        
        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        
        # Create level
        self.create_level()
        
        # Create player (start at bottom)
        self.player = Player(100, LEVEL_HEIGHT - 100, self.bullets)
        self.all_sprites.add(self.player)
        
        # Create goal (finish line at top)
        self.goal = Goal(SCREEN_WIDTH // 2 - 30, 100)
        self.all_sprites.add(self.goal)
        
        # Score
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
    
    def create_level(self):
        """Create platforms and enemies - Vertical level design"""
        # Ground platform (start point)
        ground = Platform(0, LEVEL_HEIGHT - 50, SCREEN_WIDTH, 50, 'ground')
        self.platforms.add(ground)
        self.all_sprites.add(ground)
        
        # Vertical platforming path - jarak 80-90px vertikal, posisi zigzag horizontal
        # Platform tidak overlap horizontal agar bisa lewat dengan lompat
        platforms_data = [
            # Start area - satu platform panjang di bawah
            (200, LEVEL_HEIGHT - 120, 400, 30),
            
            # Layer 1 - zigzag kiri-kanan, jarak 90px
            (50, LEVEL_HEIGHT - 210, 220, 30),
            (600, LEVEL_HEIGHT - 300, 220, 30),
            (950, LEVEL_HEIGHT - 390, 220, 30),
            
            # Layer 2 - zigzag berlawanan, jarak 90px
            (100, LEVEL_HEIGHT - 480, 220, 30),
            (500, LEVEL_HEIGHT - 570, 250, 30),
            (900, LEVEL_HEIGHT - 660, 220, 30),
            
            # Layer 3 - jarak 90px
            (50, LEVEL_HEIGHT - 750, 220, 30),
            (450, LEVEL_HEIGHT - 840, 250, 30),
            (850, LEVEL_HEIGHT - 930, 220, 30),
            
            # Layer 4 - jarak 90px
            (150, LEVEL_HEIGHT - 1020, 220, 30),
            (550, LEVEL_HEIGHT - 1110, 250, 30),
            (950, LEVEL_HEIGHT - 1200, 220, 30),
            
            # Layer 5 - jarak 90px
            (100, LEVEL_HEIGHT - 1290, 220, 30),
            (500, LEVEL_HEIGHT - 1380, 250, 30),
            (900, LEVEL_HEIGHT - 1470, 220, 30),
            
            # Layer 6 - jarak 90px
            (50, LEVEL_HEIGHT - 1560, 220, 30),
            (450, LEVEL_HEIGHT - 1650, 250, 30),
            (850, LEVEL_HEIGHT - 1740, 220, 30),
            
            # Layer 7 - jarak 90px
            (200, LEVEL_HEIGHT - 1830, 220, 30),
            (600, LEVEL_HEIGHT - 1920, 250, 30),
            (1000, LEVEL_HEIGHT - 2010, 180, 30),
            
            # Layer 8 - jarak 90px menuju goal
            (300, LEVEL_HEIGHT - 2100, 250, 30),
            (700, LEVEL_HEIGHT - 2190, 250, 30),
            
            # Final platform before goal
            (SCREEN_WIDTH // 2 - 150, 380, 300, 30),
        ]
        
        for x, y, width, height in platforms_data:
            platform = Platform(x, y, width, height, 'ground')
            self.platforms.add(platform)
            self.all_sprites.add(platform)
        
        # Create enemies - disesuaikan dengan platform zigzag (lebih sedikit)
        enemy_positions = [
            (150, LEVEL_HEIGHT - 240),
            (700, LEVEL_HEIGHT - 330),
            (1050, LEVEL_HEIGHT - 420),
            (200, LEVEL_HEIGHT - 510),
            (650, LEVEL_HEIGHT - 600),
            (1000, LEVEL_HEIGHT - 690),
            (150, LEVEL_HEIGHT - 780),
            (600, LEVEL_HEIGHT - 870),
            (950, LEVEL_HEIGHT - 960),
            (250, LEVEL_HEIGHT - 1050),
            (700, LEVEL_HEIGHT - 1140),
            (1050, LEVEL_HEIGHT - 1230),
            (200, LEVEL_HEIGHT - 1320),
            (650, LEVEL_HEIGHT - 1410),
            (1000, LEVEL_HEIGHT - 1500),
            (150, LEVEL_HEIGHT - 1590),
            (600, LEVEL_HEIGHT - 1680),
            (950, LEVEL_HEIGHT - 1770),
            (350, LEVEL_HEIGHT - 1860),
            (750, LEVEL_HEIGHT - 1950),
            (450, LEVEL_HEIGHT - 2130),
            (850, LEVEL_HEIGHT - 2220),
        ]
        
        for x, y in enemy_positions:
            enemy = Enemy(x, y, self.bullets)
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == "playing":
                        self.state = "menu"  # Kembali ke menu
                    else:
                        self.running = False
                
                # Menu screen - Start game
                if self.state == "menu":
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        self.start_game()
                
                # Game over / Victory - Back to menu
                if self.state in ["game_over", "victory"]:
                    if event.key == pygame.K_m:
                        self.state = "menu"
                        self.reset_game()
                    elif event.key == pygame.K_r:
                        self.start_game()
    
    def start_game(self):
        """Start new game"""
        self.state = "playing"
        self.reset_game()
    
    def reset_game(self):
        """Reset game variables"""
        self.game_over = False
        self.victory = False
        self.camera_y = 0
        self.score = 0
        
        # Clear all sprite groups
        self.all_sprites.empty()
        self.platforms.empty()
        self.bullets.empty()
        self.enemies.empty()
        self.explosions.empty()
        
        # Recreate level
        self.create_level()
        
        # Recreate player
        self.player = Player(100, LEVEL_HEIGHT - 100, self.bullets)
        self.all_sprites.add(self.player)
        
        # Recreate goal
        self.goal = Goal(SCREEN_WIDTH // 2 - 30, 100)
        self.all_sprites.add(self.goal)
    
    def update(self):
        if self.state != "playing":
            return
        
        if self.game_over or self.victory:
            return
        
        # Update player
        self.player.update(self.platforms)
        
        # Update camera to follow player
        self.update_camera()
        
        # Update goal
        self.goal.update()
        
        # Update enemies
        for enemy in self.enemies:
            enemy.update(self.platforms, self.player)
        
        # Update bullets
        self.bullets.update()
        
        # Update explosions
        self.explosions.update()
        
        # Check bullet collisions
        self.check_collisions()
        
        # Check game over
        if not self.player.alive:
            self.game_over = True
            self.state = "game_over"
        
        # Check if player reached goal
        if self.player.rect.colliderect(self.goal.rect) and not self.victory:
            self.victory = True
            self.state = "victory"
            self.score += 1000  # Bonus untuk mencapai goal
        
        # Check if player fall off map
        if self.player.rect.y > LEVEL_HEIGHT + 100:
            self.player.alive = False
            self.game_over = True
            self.state = "game_over"
    
    def update_camera(self):
        """Update camera to follow player vertically"""
        # Target camera position (player in center of screen)
        target_y = self.player.rect.y - SCREEN_HEIGHT // 2
        
        # Clamp camera to level bounds
        target_y = max(0, min(target_y, LEVEL_HEIGHT - SCREEN_HEIGHT))
        
        # Smooth camera movement
        self.camera_y += (target_y - self.camera_y) * 0.1
    
    def check_collisions(self):
        # Player bullets hit enemies
        for bullet in self.bullets:
            if bullet.bullet_type == 'player':
                hit_enemies = pygame.sprite.spritecollide(bullet, self.enemies, False)
                for enemy in hit_enemies:
                    enemy.take_damage(bullet.damage)
                    bullet.kill()
                    
                    # Create explosion
                    explosion = Explosion(enemy.rect.centerx, enemy.rect.centery)
                    self.explosions.add(explosion)
                    self.all_sprites.add(explosion)
                    
                    if not enemy.alive:
                        self.score += 100
        
        # Enemy bullets hit player
        for bullet in self.bullets:
            if bullet.bullet_type == 'enemy':
                if bullet.rect.colliderect(self.player.rect):
                    self.player.take_damage(bullet.damage)
                    bullet.kill()
                    
                    # Create explosion
                    explosion = Explosion(bullet.rect.centerx, bullet.rect.centery)
                    self.explosions.add(explosion)
                    self.all_sprites.add(explosion)
    
    def draw(self):
        # Draw based on game state
        if self.state == "menu":
            self.draw_menu()
            pygame.display.flip()
            return
        
        # Draw background with camera offset
        if self.background:
            self.screen.blit(self.background, (0, -self.camera_y))
        else:
            self.screen.fill((135, 206, 235))
        
        # Draw all sprites with camera offset
        for platform in self.platforms:
            screen_y = platform.rect.y - self.camera_y
            if -100 < screen_y < SCREEN_HEIGHT + 100:  # Only draw if on screen
                self.screen.blit(platform.image, (platform.rect.x, screen_y))
        
        # Draw goal
        goal_y = self.goal.rect.y - self.camera_y
        if -100 < goal_y < SCREEN_HEIGHT + 100:
            self.screen.blit(self.goal.image, (self.goal.rect.x, goal_y))
        
        for enemy in self.enemies:
            screen_y = enemy.rect.y - self.camera_y
            if -100 < screen_y < SCREEN_HEIGHT + 100:
                self.screen.blit(enemy.image, (enemy.rect.x, screen_y))
        
        for bullet in self.bullets:
            screen_y = bullet.rect.y - self.camera_y
            if -100 < screen_y < SCREEN_HEIGHT + 100:
                self.screen.blit(bullet.image, (bullet.rect.x, screen_y))
        
        for explosion in self.explosions:
            screen_y = explosion.rect.y - self.camera_y
            if -100 < screen_y < SCREEN_HEIGHT + 100:
                self.screen.blit(explosion.image, (explosion.rect.x, screen_y))
        
        if self.player.alive:
            player_y = self.player.rect.y - self.camera_y
            self.screen.blit(self.player.image, (self.player.rect.x, player_y))
        
        # Draw UI
        self.draw_ui()
        
        # Draw game over or victory screen overlay
        if self.state == "game_over":
            self.draw_game_over()
        elif self.state == "victory":
            self.draw_victory()
        
        pygame.display.flip()
    
    def draw_menu(self):
        """Draw home/welcome screen"""
        # Background gradient
        for y in range(SCREEN_HEIGHT):
            color_val = int(50 + (y / SCREEN_HEIGHT) * 100)
            pygame.draw.line(self.screen, (color_val, color_val // 2, color_val + 50), 
                           (0, y), (SCREEN_WIDTH, y))
        
        # Title
        title_font = pygame.font.Font(None, 100)
        title_text = title_font.render("CAT CLIMBER", True, (255, 200, 0))
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
        
        # Shadow effect
        shadow_text = title_font.render("CAT CLIMBER", True, (50, 50, 50))
        shadow_rect = shadow_text.get_rect(center=(SCREEN_WIDTH // 2 + 4, 104))
        self.screen.blit(shadow_text, shadow_rect)
        self.screen.blit(title_text, title_rect)
        
        # Subtitle
        subtitle_font = pygame.font.Font(None, 36)
        subtitle_text = subtitle_font.render("Vertical Platformer Adventure", True, WHITE)
        subtitle_rect = subtitle_text.get_rect(center=(SCREEN_WIDTH // 2, 160))
        self.screen.blit(subtitle_text, subtitle_rect)
        
        # Draw cute cat ASCII art or simple cat icon
        cat_y = 220
        cat_font = pygame.font.Font(None, 80)
        cat_text = cat_font.render("🐱", True, (255, 140, 60))  # Fallback jika no emoji
        try:
            cat_rect = cat_text.get_rect(center=(SCREEN_WIDTH // 2, cat_y + 40))
            self.screen.blit(cat_text, cat_rect)
        except:
            # Draw simple cat with shapes
            cat_x = SCREEN_WIDTH // 2 - 40
            cat_y = 220
            # Head
            pygame.draw.circle(self.screen, (255, 140, 60), (cat_x + 40, cat_y + 40), 35)
            # Ears
            pygame.draw.polygon(self.screen, (255, 140, 60), 
                              [(cat_x + 15, cat_y + 15), (cat_x + 25, cat_y + 5), (cat_x + 25, cat_y + 25)])
            pygame.draw.polygon(self.screen, (255, 140, 60), 
                              [(cat_x + 65, cat_y + 15), (cat_x + 55, cat_y + 5), (cat_x + 55, cat_y + 25)])
            # Eyes
            pygame.draw.circle(self.screen, (50, 50, 50), (cat_x + 30, cat_y + 35), 5)
            pygame.draw.circle(self.screen, (50, 50, 50), (cat_x + 50, cat_y + 35), 5)
            # Nose
            pygame.draw.circle(self.screen, (255, 150, 150), (cat_x + 40, cat_y + 45), 3)
        
        # Game objective
        objective_y = 340
        objective_texts = [
            "🎯 OBJECTIVE:",
            "Climb to the top and reach the GOAL flag!",
            "Defeat enemies and avoid falling!",
        ]
        
        for i, text in enumerate(objective_texts):
            color = (255, 215, 0) if i == 0 else (200, 200, 200)
            font = self.font if i == 0 else self.small_font
            obj_text = font.render(text, True, color)
            obj_rect = obj_text.get_rect(center=(SCREEN_WIDTH // 2, objective_y + i * 30))
            self.screen.blit(obj_text, obj_rect)
        
        # Controls
        controls_y = 440
        control_texts = [
            "⌨️  CONTROLS:",
            "Move: A/D or Arrow Keys",
            "Jump: W/Space/Up Arrow",
            "Shoot: X or Ctrl",
        ]
        
        for i, text in enumerate(control_texts):
            color = (255, 215, 0) if i == 0 else WHITE
            font = self.small_font if i == 0 else pygame.font.Font(None, 20)
            ctrl_text = font.render(text, True, color)
            ctrl_rect = ctrl_text.get_rect(center=(SCREEN_WIDTH // 2, controls_y + i * 25))
            self.screen.blit(ctrl_text, ctrl_rect)
        
        # Start button (animated)
        start_y = 560
        time_ms = pygame.time.get_ticks()
        alpha = int(128 + 127 * abs(pygame.math.Vector2(1, 0).rotate(time_ms * 0.2).x))
        
        start_font = pygame.font.Font(None, 48)
        start_text = start_font.render("PRESS ENTER or SPACE TO START", True, (0, 255, 0))
        start_text.set_alpha(alpha)
        start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, start_y))
        self.screen.blit(start_text, start_rect)
        
        # Credits
        credit_font = pygame.font.Font(None, 18)
        credit_text = credit_font.render("Made with Python & Pygame | ESC to Quit", True, (150, 150, 150))
        credit_rect = credit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20))
        self.screen.blit(credit_text, credit_rect)
    
    def draw_ui(self):
        # Health bar
        self.player.draw_health_bar(self.screen)
        
        # Score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (SCREEN_WIDTH - 200, 10))
        
        # Enemy count
        enemy_text = self.small_font.render(f"Enemies: {len(self.enemies)}", True, WHITE)
        self.screen.blit(enemy_text, (SCREEN_WIDTH - 200, 50))
        
        # Height progress (distance to goal)
        height = LEVEL_HEIGHT - self.player.rect.y
        progress_percent = int((height / LEVEL_HEIGHT) * 100)
        height_text = self.small_font.render(f"Progress: {progress_percent}%", True, WHITE)
        self.screen.blit(height_text, (SCREEN_WIDTH - 200, 80))
        
        # Controls
        control_texts = [
            "CLIMB TO THE TOP!",
            "Move: A/D or Arrows",
            "Jump: W/Space/Up",
            "Shoot: X or Ctrl",
            "Quit: ESC"
        ]
        
        y_offset = 80
        for i, text in enumerate(control_texts):
            color = (255, 215, 0) if i == 0 else WHITE
            control_surface = self.small_font.render(text, True, color)
            self.screen.blit(control_surface, (10, y_offset))
            y_offset += 25
    
    def draw_game_over(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game over text with larger font
        game_over_font = pygame.font.Font(None, 80)
        game_over_text = game_over_font.render("YOU LOSE!", True, RED)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80))
        self.screen.blit(game_over_text, text_rect)
        
        # Cat crying emoji or sad message
        sad_font = pygame.font.Font(None, 60)
        sad_text = sad_font.render("😿", True, WHITE)
        sad_rect = sad_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
        self.screen.blit(sad_text, sad_rect)
        
        # Score
        score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))
        self.screen.blit(score_text, score_rect)
        
        # Options
        restart_text = self.small_font.render("Press R to Restart", True, (0, 255, 0))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 90))
        self.screen.blit(restart_text, restart_rect)
        
        menu_text = self.small_font.render("Press M to Main Menu", True, (255, 215, 0))
        menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120))
        self.screen.blit(menu_text, menu_rect)
    
    def draw_victory(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Victory text with larger font
        victory_font = pygame.font.Font(None, 80)
        victory_text = victory_font.render("YOU WIN!", True, (0, 255, 0))
        text_rect = victory_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        self.screen.blit(victory_text, text_rect)
        
        # Congrats message
        congrats_text = self.font.render("Congratulations! You reached the top!", True, (255, 215, 0))
        congrats_rect = congrats_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(congrats_text, congrats_rect)
        
        # Happy cat emoji
        happy_font = pygame.font.Font(None, 60)
        happy_text = happy_font.render("😺", True, WHITE)
        happy_rect = happy_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
        self.screen.blit(happy_text, happy_rect)
        
        # Score
        score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70))
        self.screen.blit(score_text, score_rect)
        
        # Options
        restart_text = self.small_font.render("Press R to Play Again", True, (0, 255, 0))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120))
        self.screen.blit(restart_text, restart_rect)
        
        menu_text = self.small_font.render("Press M to Main Menu", True, (255, 215, 0))
        menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        self.screen.blit(menu_text, menu_rect)
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
