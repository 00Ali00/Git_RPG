import pygame
WIDTH = 600
HEIGHT = 600
FPS = 60
TILESIZE = 32

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('RPG')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

fl_Start = True
while fl_Start:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fl_Start = False

    all_sprites.update()
    screen.fill('black')
    all_sprites.draw(screen)