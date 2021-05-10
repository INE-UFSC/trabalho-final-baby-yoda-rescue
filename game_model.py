import pygame as pg
import random
from player import Player
from protipo.level import Level
from prototipo.configs import *


class GameModel:
    def __init__(self):
        self.__FPS = FPS
        self.__player = Player()
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
