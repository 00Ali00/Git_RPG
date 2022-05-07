import pygame
from settings import *
from player import Player

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('RPG')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

fl_Start = True
while fl_Start:
    delta_time = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fl_Start = False

    all_sprites.update(delta_time)
    screen.fill('black')
    all_sprites.draw(screen)
    pygame.display.flip()