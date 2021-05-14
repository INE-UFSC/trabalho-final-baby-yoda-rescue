from abc import ABC, abstractmethod
from configs import *


class CharPhysics(ABC):
    def __init__(self):
        self.__std_acc = 0.3  # aceleracao padrao
        self.__jump_acc = -4  # aceleracao pulo
        self.__fric = -0.09  # atrito
        self.__max_vel = 10
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

    def char_physics(self):

        # gravidade e colisao inferior
        if not self.collisions["bottom"]:
            self.acc += pg.math.Vector2(
                0, 0.01)  # adiciona gravidade a y

        if self.collisions["bottom"]:
            self.acc.y = 0
            self.vel.y = 0
            # definie a posição acima da plataforma
            self.pos.y = self.collisions["bottom"]

        # equacoes de movimento
        self.vel.x += self.vel.x * self.fric

        self.vel += self.acc

        self.pos += self.vel

        # velocidade max
        if self.vel.x > self.__max_vel:
            self.vel.x = self.__max_vel
        if self.vel.x < -self.__max_vel:
            self.vel.x = -self.__max_vel

        if self.vel.y > self.__max_vel:
            self.vel.y = self.__max_vel

        if self.vel.y < -self.__max_vel:
            self.vel.y = -self.__max_vel

        # Updates do player:
        # Posição do player marcada como ponto do meio inferior
        self.rect.midbottom = self.pos
