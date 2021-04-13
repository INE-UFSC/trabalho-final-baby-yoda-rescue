import pygame as pg
from configs import *

vec = pg.math.Vector2


class Jogador(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.__image = pg.Surface((50, 50))
        self.__image.fill((0, 0, 255))
        self.__rect = self.__image.get_rect()
        self.__rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.__vel = vec(0, 0)
        self.__acc = vec(0, 0)
        self.__padraoacc = 0.5
        # criar classe FisicaObj
        self.__fric = - 0.05
        self.__res = - 0.001
        self.__gravidade = 0.001

    def update(self):
        self.acc = vec(0, self.__gravidade)
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.acc.x = -1 * self.padraoacc

        if keys[pg.K_RIGHT]:
            self.acc.x = self.padraoacc

        if keys[pg.K_UP]:
            self.acc.y = -1 * self.padraoacc

        if keys[pg.K_DOWN]:
            self.acc.y = self.padraoacc

        # aplica friccao ao eixo x
        self.acc.x += self.vel.x * self.__fric

        # aplica resistencia do ar ao eixo y
        self.acc.x += self.vel.x * self.__res

        # equacoes de movimento
        self.vel += self.acc
        self.pos += self.vel + self.padraoacc * self.acc

        self.rect.center = self.pos

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, n):
        self.__rect = n

    @property
    def vel(self):
        return self.__vel

    @property
    def acc(self):
        return self.__acc

    @property
    def padraoacc(self):
        return self.__padraoacc

    @vel.setter
    def vel(self, n):
        self.__vel = n

    @acc.setter
    def acc(self, n):
        self.__acc = n

    @padraoacc.setter
    def padraoacc(self, n):
        self.__padraoacc = n
