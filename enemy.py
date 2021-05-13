from configs import *

class Enemy(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.__size = (32, 48)
        self.__health = 100
        self.__pos = pos  # deve ser definido pelo level
        self.__vel = vec(0, 0)  # velocidade
        self.__acc = vec(0, 0)  # aceleracao
        self.__std_acc = 0.5  # aceleracao padrao
        self.__image = pg.Surface(self.__size)
        self.__image.fill(WHITE)
        self.__rect = self.__image.get_rect()
        self.__rect.midbottom = self.__pos

    @ property
    def image(self):
        return self.__image

    @ property
    def rect(self):
        return self.__rect

    @ property
    def size(self):
        return self.__size

    @ size.setter
    def size(self, n):
        self.__size = n

    @ property
    def pos(self):
        return self.__pos

    @ pos.setter
    def pos(self, n):
        self.__pos = n

    @ property
    def vel(self):
        return self.__vel

    @ vel.setter
    def vel(self, n):
        self.__vel = n

    @ property
    def acc(self):
        return self.__acc

    @ acc.setter
    def acc(self, n):
        self.__acc = n

    @ property
    def std_acc(self):
        return self.__std_acc

    @ property
    def jump_acc(self):
        return self.__jump_acc

    @ property
    def key(self):
        return self.__key

    @ key.setter
    def key(self, n):
        self.__key = n

    @ property
    def health(self):
        return self.__health

    @ health.setter
    def health(self, n):
        self.__health = n
