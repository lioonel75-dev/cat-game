import pygame, sys
font = pygame.font.Font(None,50)


BUTTONS = {
"easy": pygame.Rect(300,200,200,60),
"medium": pygame.Rect(300,300,200,60),
"hard": pygame.Rect(300,400,200,60)
}


def draw_button(text, rect):
    pygame.draw.rect(screen,(200,200,200),rect)
    label = font.render(text,True,(0,0,0))
    screen.blit(label,(rect.x+20,rect.y+10))


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            for lvl,rect in BUTTONS.items():
                if rect.collidepoint(e.pos):
                    import game
                    game.start(lvl)


    screen.fill((100,150,250))
    for lvl,rect in BUTTONS.items(): draw_button(lvl.upper(),rect)
    pygame.display.flip()






 