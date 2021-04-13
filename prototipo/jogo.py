import pygame as pg
import random
from jogador import Jogador
from configs import *
from level import Level


class Jogo:
    def __init__(self):
        # configs
        self.__FPS = FPS
        self.__caption = TITULO
        self.__sprites = pg.sprite.Group()  # Caz vai verificar
        self.__jogador = Jogador()
        self.__level = Level()

        # inicializa a janela do pygame
        pg.init()
        # inicializa o audio
        pg.mixer.init()
        # define o titulo
        pg.display.set_caption(self.__caption)
        # define o clock
        self.__clock = pg.time.Clock()
        # adiciona sprites ao grupo sprites
        self.__sprites.add(self.__jogador)
        self.__screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.__running = True

    def run(self):
        self.__running = True
        while self.__running:
            # sincroniza o loop com o clock
            self.__clock.tick(self.__FPS)

            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()

    def events(self):
        # eventos
        for event in pg.event.get():
            # se fecha a janela termina o programa
            if event.type == pg.QUIT:
                self.__running = False

    def update(self):

        # Logica de colisão
        # plataformas
        # Codigo de controlado_jogo
        hits_plataforms = pg.sprite.groupcollide(
            self.level.platforms,
            self.__jogador, False, False)

        if self.vel.y > 0:
            if hits_plataforms:
                if self.pos.y < hits_plataforms[0].rect.bottom:
                    self.pos.y = hits_plataforms[0].rect.top + 1
                    self.vel.y = 0
                    self.jumping = False
                # print(hits_plataforms[0].rect.bottom)

        hits_walls = pg.sprite.spritecollide(self, walls, False)
        if self.vel.y > 0:
            if hits_walls:
                if self.pos.y > hits_walls[0].rect.bottom:
                    self.pos.y = hits_walls[0].rect.top + 1
                    self.vel.y = 0
                    self.jumping = False
                # print(hits_walls[0].rect.bottom)
        if self.vel.x > 0:
            if hits_walls:
                print(f'self.pos.x RIGHT = {hits_walls[0].rect.right}')
                if self.pos.x < (hits_walls[0].rect.right):
                    self.pos.x = hits_walls[0].rect.right - (self.size[0])
                    self.vel.x = 0
        if self.vel.x < 0:
            if hits_walls:
                print(f'self.pos.x LEFT = {hits_walls[0].rect.left}')
                if self.pos.x > (hits_walls[0].rect.left):
                    self.pos.x = (hits_walls[0].rect.left) + (self.size[0])
                    self.vel.x = 0

        self.__sprites.update()

    def draw(self):
        self.__screen.fill((255, 255, 255))
        self.__sprites.draw(self.__screen)

        # realiza o flip apos desenhar tudo
        pg.display.flip()

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, new_value):
        self.__running = new_value

    @property
    def clock(self):
        return self.__clock

    @property
    def level(self):
        return self.__level
