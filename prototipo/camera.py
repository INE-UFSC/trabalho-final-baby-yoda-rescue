import pygame as pg
from pygame import *
from configs import *


class Camera():
    def __init__(self, jogador, level):
        super().__init__()
        self.__jogador = jogador #personagem
        self.__level = level

    def update(self):
        if self.__jogador.rect.right > WIDTH / 2:
            self.__jogador.pos.x -= abs(self.__jogador.vel.x)
            for platf in self.__level.platforms:
                platf.rect.x -= abs(self.__jogador.vel.x)
        elif self.__jogador.rect.left < WIDTH / 2:
            self.__jogador.pos.x += abs(self.__jogador.vel.x)
            for platf in self.__level.platforms:
                platf.rect.x += abs(self.__jogador.vel.x)
        
        if self.__jogador.rect.top <= HEIGHT / 4:
            self.__jogador.pos.y += abs(self.__jogador.vel.y)
            for platf in self.__level.platforms:
                platf.rect.y += abs(self.__jogador.vel.y)
        elif self.__jogador.rect.bottom > HEIGHT - 50:
            self.__jogador.pos.y -= abs(self.__jogador.vel.y)
            for platf in self.__level.platforms:
                platf.rect.y -= abs(self.__jogador.vel.y)
