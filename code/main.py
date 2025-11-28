

# ===== FILE: game.py =====
import pygame, sys
from enemy import Enemy
from bullet import Bullet

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
CAT_SPRITE = pygame.Surface((40,40)); CAT_SPRITE.fill((255,200,0))


def start(level="easy"):
    settings = {
        "easy": {"time":30,"enemy_count":4,"enemy_speed":2,"ammo":12,"shoot_delay":300},
        "medium": {"time":20,"enemy_count":6,"enemy_speed":3,"ammo":8,"shoot_delay":400},
        "hard": {"time":12,"enemy_count":10,"enemy_speed":4,"ammo":5,"shoot_delay":500},
    }

    data = settings[level]
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    cat = CAT_SPRITE.get_rect(center=(400,300))

    for i in range(data["enemy_count"]):
        enemies.add(Enemy(data["enemy_speed"], "vertical" if i%2==0 else "horizontal"))

    ammo = data["ammo"]
    last_shot = 0
    start_ticks = pygame.time.get_ticks()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                now = pygame.time.get_ticks()
                if ammo>0 and now-last_shot>=data["shoot_delay"]:
                    bullets.add(Bullet(cat.centerx,cat.centery,"up"))
                    ammo-=1
                    last_shot = now

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: cat.x-=4
        if keys[pygame.K_RIGHT]: cat.x+=4
        if keys[pygame.K_UP]: cat.y-=4
        if keys[pygame.K_DOWN]: cat.y+=4

        enemies.update(); bullets.update()

        elapsed=(pygame.time.get_ticks()-start_ticks)//1000
        if elapsed>=data["time"]: print("Time up!"); return

        pygame.sprite.groupcollide(bullets,enemies,True,True)
        if len(enemies)==0: print("You win!"); return

        tile=40
        for y in range(0,600,tile):
            for x in range(0,800,tile):
                c=(70,70,70) if (x//tile+y//tile)%2==0 else (90,90,90)
                pygame.draw.rect(screen,c,(x,y,tile,tile))

        screen.blit(CAT_SPRITE,cat)
        enemies.draw(screen)
        bullets.draw(screen)

        f=pygame.font.Font(None,40)
        screen.blit(f.render(f"Time: {data['time']-elapsed}",True,(255,255,255)),(20,20))
        screen.blit(f.render(f"Ammo: {ammo}",True,(255,255,0)),(20,60))

        pygame.display.flip(); clock.tick(60)
