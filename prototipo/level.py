from typing import Tuple
import pygame as pg


class Level:
    def __init__(self):
        self.__platforms: []
        self.__bg: Tuple(255, 255, 255)

    @property
    def platforms(self):
        return self.__platforms

    @property
    def bg(self):
        return self.__bg
