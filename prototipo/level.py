from typing import Tuple
import pygame as pg

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
        self.__platforms: list[floor, plat1, plat2, plat3, wall1]
        self.__bg: Tuple(255, 255, 255)

    @property
    def platforms(self):
        return self.__platforms

    @property
    def bg(self):
        return self.__bg
