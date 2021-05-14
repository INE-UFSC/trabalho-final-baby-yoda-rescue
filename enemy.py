from configs import *
from char_physics import CharPhysics
import pygame as pg
from pygame import math
from abstest import abstest


class Enemy(CharPhysics, pg.sprite.Sprite):
    def __init__(self, x, y, lista_):
        pg.sprite.Sprite.__init__(self)  # inicaliza o sprite do pygame
        super().__init__()  # super nao inicializa pg.sprite.Sprite por algum motivo
        self.__health = 100
        self.__pos = vec(x, y)
        self.__vel = vec(0, 0)
        self.__acc = vec(0, 0)

        self.__lista = lista_
        self.__sprites = []

        self.load_sprite()

        self.__current_sprite = 4

        self.__image = self.__sprites[self.__current_sprite]
        self.__rect = self.__image.get_rect()
        self.__rect.midbottom = self.__pos

        self.animation("idle")

    def load_sprite(self):
        for image in range(len(self.__lista)):
            self.__sprites.append(pg.image.load(data + self.__lista[image]))

    def animation(self, command):
        if self.vel.x < 0:  # and not self.colisions['left']:
            self.__current_sprite -= 0.3
            if self.__current_sprite <= 0:
                self.__current_sprite = 3
        elif self.vel.x > 0:  # and not self.colisions['right']:
            self.__current_sprite += 0.3
            if self.__current_sprite >= len(self.__sprites):
                self.__current_sprite = 5
        else:
            self__current_sprite = 4

        self.__image = self.__sprites[int(self.__current_sprite)]

    def vai_e_volta(self):
        self.vel.x -= 5
        pg.time.wait(5000)
        self.vel.y += 5

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
    def health(self):
        return self.__health

    @ health.setter
    def health(self, n):
        self.__health = n

    @ property
    def current_sprite(self):
        return self.__current_sprite
