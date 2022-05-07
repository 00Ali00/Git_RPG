import pygame

WIDTH = 600
HEIGHT = 600
FPS = 60
TILESIZE = 32

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.move_x, self.move_y = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.move_y -= 3
        if keys[pygame.K_DOWN]:
            self.move_y += 3
        if keys[pygame.K_LEFT]:
            self.move_x -= 3
        if keys[pygame.K_RIGHT]:
            self.move_x += 3
        self.rect.x += self.move_x
        self.rect.y += self.move_y


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
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fl_Start = False

    all_sprites.update()
    screen.fill('black')
    all_sprites.draw(screen)
    pygame.display.flip()