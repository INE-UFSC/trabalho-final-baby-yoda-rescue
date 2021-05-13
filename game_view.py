import pygame as pg
import random
from camera import Camera
from prototipo.configs import *


class GameView:
    def __init__(self, player, level, sprites, attacks):
        self.__screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.__player = player
        self.__level = level
        self.__sprites = sprites
        self.__caption = pg.display.set_caption(TITULO)
        self.__camera = Camera(self.__player, self.__level)
        self.__attacks = attacks
        self.__background = pg.image.load(
            "teste.png") # provisorio MUDAR ENDERECO
        self.__bg_x = 0
        self.__rel_x = None

    def draw(self):
        self.bg_movement()
        # desenha todos os sprites OTIMIZAR para sprites individuais
        #print(self.__sprites.sprites()[0].rect.midbottom, self.__sprites.sprites()[0].pos)
        self.__sprites.draw(self.__screen)
        # realiza o flip apos desenhar tudo
        pg.display.flip()

    def update_attacks(self):
        self.__sprites.add(self.__attacks)

    def bg_movement(self):

        # lógica do movimento do background
        self.__rel_x = self.__bg_x % self.__background.get_rect().width  # avaliar repeticoes
        self.__screen.blit(self.__background, [
            self.__rel_x - self.__background.get_rect().width, 0])
        # replicacao do bg
        if self.__rel_x < WIDTH:
            self.__screen.blit(self.__background, (self.__rel_x, 0))
        # movimento do bg
        self.__bg_x -= 1

    def update_scene(self):

        # Adiciona sprites ao grupo principal de sprites
        self.__sprites.add(
            self.__player, self.__level.platforms,
            self.__level.items, self.__level.exit,
            self.__level.enemies, self.__attacks)

        if (self.__player.pos.x - (self.__player.size[0]/2) > WIDTH):

            self.__level.next()
            self.__level.update()
            self.__player.pos.x = WIDTH / 6  # varia, cuidar com os pixeis de cada fase
            self.__player.pos.y = HEIGHT / 2.5
