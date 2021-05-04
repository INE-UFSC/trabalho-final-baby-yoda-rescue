from typing import Tuple
import pygame as pg
from platform import Platform
from key import Key
from configs import *


# deve ser o atributo arch para arquitetura de level, pensar em solucoes para baixo acoplamento
floor = Platform(0, HEIGHT - HEIGHT/30, WIDTH, HEIGHT/30, RED)
wall1 = Platform(WIDTH/3, 400, WIDTH/10, HEIGHT/30, BLUE)
wall2 = Platform(WIDTH/2, HEIGHT/2, WIDTH/10, HEIGHT/30, BLUE)
wall3 = Platform(WIDTH/2, HEIGHT/1.5, WIDTH/10, HEIGHT/30, BLUE)
wall4 = Platform(WIDTH/6, (HEIGHT - HEIGHT/2) - HEIGHT/30, WIDTH/40, HEIGHT/2, BLUE)


class Level:
    def __init__(self, world):
        self.__world = world
        self.__platforms = pg.sprite.Group()
        self.__items = pg.sprite.Group()
        self.__bg = (BLUE)

        row_count = 0
        for row in self.__world:
            col_count = 0
            for tile in row:
                if tile == 1:
                    wall = Platform(col_count * TILE_SIZE_W, row_count * TILE_SIZE_H, TILE_SIZE_W, TILE_SIZE_H, BLUE)
                    self.__platforms.add(wall)
                    #tile = (wall.image, wall.rect)
                elif tile == 2:
                    grogu = Key(col_count * TILE_SIZE_W, row_count * TILE_SIZE_H, 20, 20, GREEN)
                    self.__items.add(grogu)
                col_count += 1
            row_count += 1

        self.__spawn_point = ((WIDTH, HEIGHT))
        #self.__platforms.add(floor, wall1, wall2, wall3, wall4)
        

    @property
    def world(self):
        return self.__world
    
    @property
    def platforms(self):
        return self.__platforms

    @property
    def items(self):
        return self.__items

    @property
    def bg(self):
        return self.__bg
