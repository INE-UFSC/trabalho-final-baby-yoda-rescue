from typing import Tuple
import pygame as pg
from platform import Platform
from key import Key
from extraction_point import Extraction_point
from configs import *
from enemy import Enemy


class Level:
    def __init__(self, world):
        self.__world = world
        self.__current = self.__world[0]
        self.__platforms = pg.sprite.Group()
        self.__items = pg.sprite.Group()
        self.__exit = pg.sprite.Group()
        self.__enemies = pg.sprite.Group()
        self.__bg = (BLUE)
        self.__spawn_point = ((WIDTH/2, HEIGHT/2))  # apenas para evitar bugs

        # escaneia tile map
        row_count = 0
        for row in self.__current:
            col_count = 0
            for tile in row:
                # adiciona plataformas
                if tile == 1:

                    wall = Platform(col_count * TILE_SIZE_W, row_count *
                                    TILE_SIZE_H, TILE_SIZE_W, TILE_SIZE_H, BLUE)
                    self.__platforms.add(wall)
                    # tile = (wall.image, wall.rect)

                # adiciona grogu/key
                elif tile == 2:
                    grogu = Key(col_count * TILE_SIZE_W,
                                row_count * TILE_SIZE_H, 20, 20, GREEN)
                    self.__items.add(grogu)
                # adiciona fim da faze
                elif tile == 3:
                    ship = Extraction_point(
                        col_count * TILE_SIZE_W, row_count * TILE_SIZE_H, TILE_SIZE_W, TILE_SIZE_H, PURPLE)
                    self.__exit.add(ship)

                # adiciona inimigo
                elif tile == 4:
                    storm_trooper = Enemy(
                        (col_count * TILE_SIZE_W, row_count * TILE_SIZE_H))
                    self.__enemies.add(storm_trooper)

                # adiciona spawn point
                elif tile == 5:
                    self.__spawn_point = (
                        (col_count * TILE_SIZE_W, row_count * TILE_SIZE_H))

                col_count += 1
            row_count += 1

    
    def next(self):
        index = self.__world.index(self.__current)
        print(index)
        if index < len(self.__world):
            self.__current = world[index+1]

    @ property
    def current(self):
        return self.__current

    @ property
    def world(self):
        return self.__world

    @ property
    def platforms(self):
        return self.__platforms

    @ property
    def items(self):
        return self.__items

    @ property
    def exit(self):
        return self.__exit

    @ property
    def bg(self):
        return self.__bg

    @ property
    def spawn_point(self):
        return self.__spawn_point

    @ property
    def enemies(self):
        return self.__enemies
