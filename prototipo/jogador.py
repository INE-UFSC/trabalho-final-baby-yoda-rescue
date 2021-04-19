from configs import *
import pygame as pg


vec = pg.math.Vector2


class Jogador(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.__image = pg.Surface((32, 48))
        self.__image.fill(WHITE)
        self.__rect = self.__image.get_rect()
        self.__rect.center = (WIDTH / 2, HEIGHT / 2)
        self.__pos = vec(WIDTH / 2, HEIGHT / 2)
        self.__vel = vec(0, 0)
        self.__acc = vec(0, 0)
        self.__padraoacc = 0.5
        # criar classe FisicaObj
        self.__fric = -0.12 # -0.05
        self.__gravidade = 0.5 # 1
        self.__plat_collide = False

    # modificar parâmetros para
    def update(self):
        self.acc = vec(0, self.__gravidade)
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.acc.x = -1 * self.padraoacc
        if keys[pg.K_RIGHT]:
            self.acc.x = self.padraoacc
        
        # Remove o Bug visual da gravidade ao colidir com plataformas
        if self.__plat_collide == True:
            self.vel.y = 0
        if keys[pg.K_SPACE] and self.__plat_collide == True:
            self.vel.y = -14
        
        # aplica friccao ao eixo x
        self.acc.x += self.vel.x * self.__fric

        # equacoes de movimento
        self.vel += self.acc
        self.pos += self.vel + self.padraoacc * self.acc

        # mudado conforme parte 3 do tutorial por motivos de simplificacao
        self.rect.midbottom = self.pos

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

    @property
    def pos(self):
        return self.__pos

    @property
    def plat_collide(self):
        return self.__plat_collide

    @pos.setter
    def pos(self, n):
        self.__pos = n

    @vel.setter
    def vel(self, n):
        self.__vel = n

    @acc.setter
    def acc(self, n):
        self.__acc = n

    @padraoacc.setter
    def padraoacc(self, n):
        self.__padraoacc = n

    @plat_collide.setter
    def plat_collide(self, n):
        self.__plat_collide = n
