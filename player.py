from configs import *
from char_physics import CharPhysics
import pygame as pg
from pygame import math


# LOAD_SPRITE e ANIMATION CharView
# Toda a fisica padrao vem de CharPhysics
class Player(CharPhysics, pg.sprite.Sprite):
    def __init__(self, lista):
        pg.sprite.Sprite.__init__(self)  # inicaliza o sprite do pygame
        super().__init__()  # super nao inicializa pg.sprite.Sprite por algum motivo
        self.__health = 1000
        self.__size = (32, 48)
        self.__key = False
        self.__list = lista
        self.__sprites = []
        # persistencia
        self.__pos = vec(0, 0)  # deve ser definido pelo level
        self.__vel = vec(0, 0)  # velocidade
        self.__acc = vec(0, 0)  # aceleracao

        self.load_sprite()

        self.__current_sprite = 4  # idle
        self.__image = self.__sprites[self.__current_sprite]
        self.__rect = self.__image.get_rect()

        self.animation("idle")

    def load_sprite(self):
        for image in range(len(self.__list)):
            self.__sprites.append(pg.image.load(data + self.__list[image]))

    def animation(self, command):
        if command == "left":  # and not self.colisions['left']:
            self.__current_sprite -= 0.3
            if self.__current_sprite <= 0:
                self.__current_sprite = 3
        elif command == "right":  # and not self.colisions['right']:
            self.__current_sprite += 0.3
            if self.__current_sprite >= len(self.__sprites):
                self.__current_sprite = 5
        else:
            self__current_sprite = 4

        self.__image = self.__sprites[int(self.__current_sprite)]

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
    def key(self):
        return self.__key

    @ key.setter
    def key(self, n):
        self.__key = n

    @ property
    def health(self):
        return self.__health

    @ health.setter
    def health(self, ht):
        self.__health = ht
