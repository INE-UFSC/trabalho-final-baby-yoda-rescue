from typing import Tuple
import pygame as pg
from platform import Platform
from configs import *

floor = Platform('floor', (WIDTH, 20), (RED), (WIDTH/2, HEIGHT - 10))
plat1 = Platform('platform1', (WIDTH/5, 20), (RED),
                 (WIDTH/4, HEIGHT * 0.75 - 20))
plat2 = Platform('platform1', (WIDTH/5, 20), (RED),
                 (WIDTH/4, HEIGHT * 0.50 - 20))
plat3 = Platform('platform1', (WIDTH/5, 20), (RED),
                 (WIDTH/4, HEIGHT * 0.25 - 20))
wall1 = Platform('wall1', (20, HEIGHT*0.75 + 10), (BLUE),
                 (WIDTH/4 + (WIDTH/5)/2, HEIGHT/2 + 50))


class Level:
    def __init__(self):
        self.__platforms: pg.sprite.Group()
        self.__walls: pg.sprite.Groupe()
        self.__bg: Tuple(255, 255, 255)
        self.__spawn: 

    def load(self):
        self.__platforms.add(floor, plat1, plat2, plat3)
        self.__walls.add(wall1)

    @property
    def platforms(self):
        return self.__platforms

    @property
    def bg(self):
        return self.__bg


all_sprites = pygame.sprite.Group()
all_sprites.add(P1, level_plataforms, level_walls)
