import pygame as pg
import os
from configs import dicionario

cwd = os.getcwd()
data = os.path.join(cwd, "data", "")

class Animation():
    def __init__(self, lista):        
        # VIEW

        self.__list = lista
        self.__sprites = []

        # imagens - VIEW
        for image in range(len(self.__list)):
            print(self.__list[image])
            self.__sprites.append(pg.image.load(data + self.__list[image]))

        # Criar classe no model para conter o DB das imagens
        # Criar classe no controller para carregar as imagens

        self.__current_sprite = 4  #idle
        self.__image = self.__sprites[self.__current_sprite]

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]: #and not self.colisions['left']:
            self.__current_sprite -= 0.3
            if self.__current_sprite <= 0:
                self.__current_sprite = 3

        if keys[pg.K_RIGHT]: #and not self.colisions['right']:
            self.__current_sprite += 0.3
            if self.__current_sprite >= len(self.__sprites):
                self.__current_sprite = 5

        self.__image = self.__sprites[int(self.__current_sprite)]

    @property
    def image(self):
        return self.__image

    @property
    def current_sprite(self):
        return self.__current_sprite

    @property
    def sprites(self):
        return self.__sprites