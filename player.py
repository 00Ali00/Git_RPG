import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/player.png')
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT / 2
        self.sprite_position = 0
        self.move_per_second = 120

    def update(self, delta_time):
        self.sprite_position += self.move_per_second * delta_time
        if self.sprite_position > WIDTH:
            self.sprite_position = 0
        self.rect.x = self.sprite_position
        # self.move_x, self.move_y = 0, 0
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP]:
        #     self.move_y -= 3
        # if keys[pygame.K_DOWN]:
        #     self.move_y += 3
        # if keys[pygame.K_LEFT]:
        #     self.move_x -= 3
        # if keys[pygame.K_RIGHT]:
        #     self.move_x += 3
        # if self.move_y != 0 and self.move_x != 0:
        #     self.move_y /= 1.414
        #     self.move_x /= 1.414
        # self.rect.x += self.move_x 
        # self.rect.y += self.move_y 
