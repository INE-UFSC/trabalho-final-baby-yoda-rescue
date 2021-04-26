from configs import *
import pygame as pg
import os

vec = pg.math.Vector2


class Jogador(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.size = (32, 48)
        cwd = os.getcwd()
        print("%s/asd" % cwd)
        self.__sprites = []

        # importacao de imagens
        print(("trabalho-final-grupo-5-forca\prototipo\data\mando-esquerda-4.png"))
        # teria como arrumar com o glob esses appends dos sprites, mas pode ser algo futuro
        self.__sprites.append(pg.image.load(
            "./trabalho-final-grupo-5-forca/prototipo/data/mando-esquerda-4.png"))
        self.__sprites.append(pg.image.load(
            "./trabalho-final-grupo-5-forca/prototipo/data/mando-esquerda-3.png"))
        self.__sprites.append(pg.image.load(
            "./trabalho-final-grupo-5-forca/prototipo/data/mando-esquerda-2.png"))
        self.__sprites.append(pg.image.load(
            "./trabalho-final-grupo-5-forca/prototipo/data/mando-esquerda-1.png"))
        self.__sprites.append(pg.image.load(
            "./trabalho-final-grupo-5-forca/prototipo/data/mando-idle.png"))
        self.__sprites.append(pg.image.load(
            "./trabalho-final-grupo-5-forca/prototipo/data/mando-direita-1.png"))
        self.__sprites.append(pg.image.load(
            "./trabalho-final-grupo-5-forca/prototipo/data/mando-direita-2.png"))
        self.__sprites.append(pg.image.load(
            "./trabalho-final-grupo-5-forca/prototipo/data/mando-direita-3.png"))
        self.__sprites.append(pg.image.load(
            "./trabalho-final-grupo-5-forca/prototipo/data/mando-direita-4.png"))

        self.__current_sprite = 4  # idle
        self.__image = self.__sprites[self.__current_sprite]
        self.__rect = self.__image.get_rect()
        self.__pos = vec(WIDTH / 2, HEIGHT / 2)

        self.__vel = vec(0, 0)
        self.__acc = vec(0, 0)
        self.padraoacc = 0.5
        # criar classe FisicaObj
        self.__fric = -0.12
        self.gravidade = 0.5
        self.__plat_collide = False

    # modificar parâmetros para
    def update(self):

        self.rect.midbottom = self.__pos
        self.acc = vec(0, self.gravidade)
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.acc.x = -1 * self.padraoacc

            self.__current_sprite -= 0.3
            if self.__current_sprite <= 0:
                self.__current_sprite = 3

        if keys[pg.K_RIGHT]:
            self.acc.x = self.padraoacc

            self.__current_sprite += 0.3
            if self.__current_sprite >= len(self.__sprites):
                self.__current_sprite = 5

        if keys[pg.K_SPACE] and self.__plat_collide == True:
            self.vel.y = -14

        # aplica friccao ao eixo x
        self.acc.x += self.vel.x * self.__fric

        # equacoes de movimento
        if self.vel[1] > 10:  # Limitar a aceleração da gravidade
            self.vel[1] = 10
        self.vel += self.acc
        self.pos += self.vel + self.padraoacc * self.acc

        self.__image = self.__sprites[int(self.__current_sprite)]

    @ property
    def image(self):
        return self.__image

    @ property
    def rect(self):
        return self.__rect

    @ rect.setter
    def rect(self, n):
        self.__rect = n

    @ property
    def vel(self):
        return self.__vel

    @ property
    def acc(self):
        return self.__acc

    @ property
    def padraoacc(self):
        return self.__padraoacc

    @ property
    def pos(self):
        return self.__pos

    @ property
    def plat_collide(self):
        return self.__plat_collide

    @ pos.setter
    def pos(self, n):
        self.__pos = n

    @ vel.setter
    def vel(self, n):
        self.__vel = n

    @ acc.setter
    def acc(self, n):
        self.__acc = n

    @ padraoacc.setter
    def padraoacc(self, n):
        self.__padraoacc = n

    @ plat_collide.setter
    def plat_collide(self, n):
        self.__plat_collide = n
