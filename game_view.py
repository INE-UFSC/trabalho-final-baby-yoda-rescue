import pygame as pg
import random
from camera import Camera
from prototipo.configs import *


class GameView:
    def __init__(self):

        self.__screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.__caption = TITULO
        self.__sprites = pg.sprite.Group()
        self.__camera = Camera(self.__jogador, self.__level)
        self.__background = pg.image.load("data/teste.png")
        self.__bg_x = 0
        self.__rel_x = self.__bg_x % self.__background.get_rect().width

        # inicializa a janela do pygame
        pg.init()
        # inicializa o audio
        pg.mixer.init()
        # define o titulo
        pg.display.set_caption(self.__caption)

        # VIEW
        self.__sprites.add(
            self.__jogador, self.__level.platforms, self.__level.items, self.__level.exit)

        self.__sprites.draw(self.__screen)
        # realiza o flip apos desenhar tudo
        pg.display.flip()

        def draw(self):
            # view.rodar
            # lógica de replicação e movimento do background

            self.__screen.blit(self.__background, [
                self.__rel_x - self.__background.get_rect().width, 0])
            if self.__rel_x < WIDTH:
                self.__screen.blit(self.__background, (self.__rel_x, 0))
            self.__bg_x -= 1

        self.__sprites.draw(self.__screen)
        # realiza o flip apos desenhar tudo
        pg.display.flip()
