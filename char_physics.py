from abc import ABC, abstractmethod
from configs import *


class CharPhysics(ABC):
    def __init__(self):
        self.__std_acc = 0.01  # aceleracao padrao
        self.__jump_acc = -4  # aceleracao pulo
        self.__fric = -0.001  # atrito
        self.__collisions = {"bottom": False,
                             "top": False, "right": False, "left": False}

    @ property
    def std_acc(self):
        return self.__std_acc

    @ property
    def jump_acc(self):
        return self.__jump_acc

    @ property
    def fric(self):
        return self.__fric

    @ fric.setter
    def fric(self, n):
        self.__fric = n

    @ property
    def collisions(self):
        return self.__collisions

    @ collisions.setter
    def collisions(self, n):
        self.__collisions = n
