from typing import Tuple
import pygame as pg
from platform import Platform
from key import Key
from extraction_point import Extraction_point
from configs import *


class Level:
    def __init__(self, world):
        self.__world = world
        self.__platforms = pg.sprite.Group()
        self.__items = pg.sprite.Group()
        self.__exit = pg.sprite.Group()
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
                elif tile == 3:
                    ship = Extraction_point(col_count * TILE_SIZE_W, row_count * TILE_SIZE_H, TILE_SIZE_W, TILE_SIZE_H, PURPLE)
                    self.__exit.add(ship)
                col_count += 1
            row_count += 1

        self.__spawn_point = ((WIDTH, HEIGHT))
        

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
    def exit(self):
        return self.__exit

    @property
    def bg(self):
        return self.__bg
