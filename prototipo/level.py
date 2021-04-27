from typing import Tuple
import pygame as pg
from platform import Platform
from configs import *


# deve ser o atributo arch para arquitetura de level, pensar em solucoes para baixo acoplamento
floor = Platform(0, HEIGHT - HEIGHT/30, WIDTH, HEIGHT/30, RED)
wall1 = Platform(WIDTH/3, 400, WIDTH/10, HEIGHT/30, BLUE)
wall2 = Platform(WIDTH/2, HEIGHT/2, WIDTH/10, HEIGHT/30, BLUE)
wall3 = Platform(WIDTH/2, HEIGHT/1.5, WIDTH/10, HEIGHT/30, BLUE)
wall4 = Platform(WIDTH/6, (HEIGHT - HEIGHT/2) - HEIGHT/30, WIDTH/40, HEIGHT/2, BLUE)


class Level:
    def __init__(self):
        self.__platforms = pg.sprite.Group() 
        self.__bg = (BLUE)
        self.__spawn_point = ((WIDTH, HEIGHT))
        self.__platforms.add(floor, wall1, wall2, wall3, wall4)
        

    @property
    def platforms(self):
        return self.__platforms

    @property
    def bg(self):
        return self.__bg
