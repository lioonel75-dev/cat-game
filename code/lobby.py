import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 1460, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Menu")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (60, 60, 60)
BLUE = (70, 120, 255)


font_title = pygame.font.SysFont("Arial", 60)
font_button = pygame.font.SysFont("Arial", 40)


class Button:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, self.rect, border_radius=8)
        text_surf = font_button.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)



play_btn = Button("Easy", 610, 250, 250, 60)
options_btn = Button("Hard", 610, 330, 250, 60)
quit_btn = Button("Medium", 610, 410, 250, 60)


def main_menu():
    while True:
        screen.fill(BLACK)

        
        title = font_title.render("My Game", True, BLUE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 120))

       
        play_btn.draw(screen)
        options_btn.draw(screen)
        quit_btn.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if play_btn.is_clicked(mouse_pos):
                    print("Starting game...")
                

                if options_btn.is_clicked(mouse_pos):
                    print("Options menu...")
                   

                if quit_btn.is_clicked(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()


main_menu()


 