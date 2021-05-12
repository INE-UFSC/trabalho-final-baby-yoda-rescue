from prototipo.configs import *
import pygame as pg
import os
import math
vec = pg.math.Vector2


class Lazer(pg.sprite.Sprite):
    def __init__(self, shooter, pos, mouse):
        super().__init__()
        self.__shooter = shooter
        self.__damage = 30
        self.__size = (10, 10)
        self.__pos = vec(pos)  # posicao inicial do lazer
        self.__mouse = vec(mouse)
        self.__angle = math.radians(
            math.degrees(math.atan2(self.__mouse.y - self.__pos.y, self.__mouse.x - self.__pos.x)))
        self.__vel = 10  # velocidade
        self.__image = pg.Surface(self.__size)
        self.__image.fill(RED)
        self.__rect = self.__image.get_rect()
        self.__rect.center = pos

    @ property
    def damage(self):
        return self.__damage

    @ property
    def shooter(self):
        return self.__shooter

    @ property
    def image(self):
        return self.__image

    @ property
    def rect(self):
        return self.__rect

    @ property
    def size(self):
        return self.__size

    @ size.setter
    def size(self, n):
        self.__size = n

    @ property
    def pos(self):
        return self.__pos

    @ pos.setter
    def pos(self, n):
        self.__pos = n

    @ property
    def vel(self):
        return self.__vel

    @ vel.setter
    def vel(self, n):
        self.__vel = n

    @ property
    def acc(self):
        return self.__acc

    @ acc.setter
    def acc(self, n):
        self.__acc = n

    @ property
    def std_acc(self):
        return self.__std_acc

    @ property
    def jump_acc(self):
        return self.__jump_acc

    @ property
    def key(self):
        return self.__key

    @ key.setter
    def key(self, n):
        self.__key = n

    @ property
    def angle(self):
        return self.__angle
