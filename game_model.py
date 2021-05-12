import pygame as pg
import random
from player import Player
from level import Level
from lazer import Lazer
from configs import *


class GameModel:
    def __init__(self):
        self.__FPS = FPS
        self.__player = Player()
        # implementando apenas um nivel
        self.__level = Level(world)

    @property
    def FPS(self):
        return self.__FPS

    @property
    def player(self):
        return self.__player

    @property
    def level(self):
        return self.__level

    def gen_lazer(self, pos, mouse):
        return Lazer(pos, mouse)
