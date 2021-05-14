from abc import ABC, abstractmethod
from configs import *

class Character(pg.sprite.Sprite, ABC):
    @abstractmethod
    def __init__(self):
        self.__size = (32, 48)
        self.__health = 0
        self.__pos = None 
        self.__vel = vec(0, 0)
        self.__acc = vec(0, 0)
        self.__std_acc = 0.1
        self.__jump_acc = -4

        self.__collisions = {"bottom": False,
                             "top": False, "right": False, "left": False}
    
        self.__lista = None
        self.__sprites = []

        self.__current_sprite = 4

    @abstractmethod
    def load_sprite(self):
        pass

    @abstractmethod
    def animation(self):
        pass

    @property
    @abstractmethod
    def size(self):
        pass

    @property
    @abstractmethod
    def health(self):
        pass

    @property
    @abstractmethod
    def pos(self):
        pass
    
    @property
    @abstractmethod
    def vel(self):
        pass

    @property
    @abstractmethod
    def acc(self):
        pass
    
    @property
    @abstractmethod
    def std_acc(self):
        pass

    @property
    @abstractmethod
    def jump_acc(self):
        pass

    @property
    @abstractmethod
    def current_sprite(self):
        pass

    @property
    @abstractmethod
    def collisions(self):
        pass

