import pygame as pg
from configs import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, name: str, size: tuple, color: tuple, spawn: tuple):
        super().__init__()
        self.__name = name
        self.__size = size
        self.__color = color
        self.__surf = pygame.Surface(size)
        self.__surf.fill(color)
        self.__rect = self.surf.get_rect(center = (spawn))
        
    def move(self):
        pass

