import pygame

pygame.init()
frame_size_x = 1480
frame_size_y = 720
window_screen = pygame.display.set_mode((frame_size_x, 
frame_size_y))
pygame.display.set_caption("Your game name")
clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == 
 		pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(FPS)