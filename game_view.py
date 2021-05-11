import pygame as pg
import random
from camera import Camera
from prototipo.configs import *


class GameView:
    def __init__(self, player, level, sprites):

        self.__screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.__player = player
        self.__level = level
        self.__sprites = sprites
        self.__caption = pg.display.set_caption(TITULO)
        self.__camera = Camera(self.__player, self.__level)
        self.__background = pg.image.load(
            "prototipo/data/teste.png")  # provisorio MUDAR ENDERECO
        self.__bg_x = 0
        self.__rel_x = None

        # Adiciona sprites ao grupo principal de sprites
        self.__sprites.add(
            self.__player, self.__level.platforms, self.__level.items, self.__level.exit)

    def draw(self):

        # lógica do movimento do background
        self.__rel_x = self.__bg_x % self.__background.get_rect().width
        self.__screen.blit(self.__background, [
            self.__rel_x - self.__background.get_rect().width, 0])
        # replicacao do bg
        if self.__rel_x < WIDTH:
            self.__screen.blit(self.__background, (self.__rel_x, 0))
        # movimento do bg
        self.__bg_x -= 1

        # desenha todos os sprites OTIMIZAR para sprites individuais
        self.__sprites.draw(self.__screen)
        # realiza o flip apos desenhar tudo
        pg.display.flip()
