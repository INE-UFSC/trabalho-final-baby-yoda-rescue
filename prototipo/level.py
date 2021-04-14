from typing import Tuple
import pygame as pg
from platform import Platform
from configs import *


# deve ser o atributo arch para arquitetura de level
floor = Platform(0, HEIGHT - 20, WIDTH, 20, BLUE)
wall1 = Platform(0, 0, 10, HEIGHT, RED)


class Level:
    def __init__(self):
        self.__platforms = pg.sprite.Group()
        self.__walls = pg.sprite.Group()
        self.__bg = (WHITE)
        self.__spawn_point = ((35, 52))
    # load function ?
        self.__platforms.add(floor)
        self.__walls.add(wall1)

    @property
    def platforms(self):
        return self.__platforms

    @property
    def walls(self):
        return self.__walls

    @property
    def bg(self):
        return self.__bg
