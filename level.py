from typing import Tuple
from platform import Platform
from key import Key
from extraction_point import Extraction_point
from enemy import Enemy
from configs import *


class Level:
    def __init__(self, world):
        self.__world = world
        self.__current = begin
        self.__index = 0
        self.__platforms = pg.sprite.Group()
        self.__items = pg.sprite.Group()
        self.__exit = pg.sprite.Group()
        self.__enemies = pg.sprite.Group()
        self.__bg = (BLUE)
        self.__spawn_point = ((WIDTH/2, HEIGHT/2))  # apenas para evitar bugs
        self.update()

    def next(self):
        if self.__index < len(self.__world) - 1:
            self.__index += 1
            self.__current = world[self.__index]

    def back(self):
        if self.__index >= 0:
            self.__index -= 1
            self.__current = world[self.__index]

    def update(self):
        # deleta plataformas anteriores
        for sprite in self.__platforms.sprites():
            sprite.kill()

        # remove inimigo
        for sprite in self.__enemies.sprites():
            sprite.kill()
            # escaneia tile map

        ground_img = pg.image.load("data/middle.png")
        top_ground_img = pg.image.load("data/top.png")
        bottom_groud_img = pg.image.load("data/bottom.png")

        top_left_img = pg.image.load("data/top_left.png")
        top_right_img = pg.image.load("data/top_right.png")
        bottom_left_img = pg.image.load("data/bottom_left.png")
        bottom_right_img = pg.image.load("data/bottom_right.png")

        left_ground_img = pg.image.load("data/left.png")
        right_ground_img = pg.image.load("data/right.png")

        row_count = 0
        for row in self.__current:
            col_count = 0
            for tile in row:
                # adiciona plataformas
                if tile == 1:
                    wall = Platform(col_count * TILE_SIZE_W, row_count *
                                    TILE_SIZE_H, TILE_SIZE_W+1, TILE_SIZE_H+1, ground_img)
                    self.__platforms.add(wall)
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
                        col_count * TILE_SIZE_W, row_count * TILE_SIZE_H, dicionario["enemy"])
                    self.__enemies.add(storm_trooper)
                # adiciona spawn point
                elif tile == "S":
                    self.__spawn_point = (
                        (col_count * TILE_SIZE_W, row_count * TILE_SIZE_H))
                if tile == "B":
                    wall = Platform(col_count * TILE_SIZE_W, row_count *
                                    TILE_SIZE_H, TILE_SIZE_W+1, TILE_SIZE_H+1, bottom_groud_img)
                    self.__platforms.add(wall)
                elif tile == "L":
                    wall = Platform(col_count * TILE_SIZE_W, row_count *
                                    TILE_SIZE_H, TILE_SIZE_W+1, TILE_SIZE_H+1, left_ground_img)
                    self.__platforms.add(wall)
                elif tile == "R":
                    wall = Platform(col_count * TILE_SIZE_W, row_count *
                                    TILE_SIZE_H, TILE_SIZE_W+1, TILE_SIZE_H+1, right_ground_img)
                    self.__platforms.add(wall)
                elif tile == 5:  # bottom-left
                    wall = Platform(col_count * TILE_SIZE_W, row_count *
                                    TILE_SIZE_H, TILE_SIZE_W+1, TILE_SIZE_H+1, bottom_left_img)
                    self.__platforms.add(wall)
                elif tile == 6:  # bottom-right
                    wall = Platform(col_count * TILE_SIZE_W, row_count *
                                    TILE_SIZE_H, TILE_SIZE_W+1, TILE_SIZE_H+1, bottom_right_img)
                elif tile == 7:  # top-left
                    wall = Platform(col_count * TILE_SIZE_W, row_count *
                                    TILE_SIZE_H, TILE_SIZE_W+1, TILE_SIZE_H+1, top_left_img)
                    self.__platforms.add(wall)
                elif tile == 8:  # top-right
                    wall = Platform(col_count * TILE_SIZE_W, row_count *
                                    TILE_SIZE_H, TILE_SIZE_W+1, TILE_SIZE_H+1, top_right_img)
                    self.__platforms.add(wall)
                elif tile == 9:
                    wall = Platform(col_count * TILE_SIZE_W, row_count *
                                    TILE_SIZE_H, TILE_SIZE_W+1, TILE_SIZE_H+1, top_ground_img)
                    self.__platforms.add(wall)
                # adiciona grogu/key

                col_count += 1
            row_count += 1

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
