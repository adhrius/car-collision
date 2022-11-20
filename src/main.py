import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.clock()

# Predefined some colors
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class ENEMY(pygame.sprite.sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ENEMY.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0)

    def draw(self, surface):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

            