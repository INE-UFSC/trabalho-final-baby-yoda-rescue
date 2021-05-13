from configs import *

class Lazer(pg.sprite.Sprite):
    def __init__(self, shooter, pos, mouse):
        super().__init__()
        self.__shooter = shooter
        self.__damage = 30
        self.__size = (10, 10)
        self.__pos = vec(pos)  # posicao inicial do lazer
        self.__mouse = vec(mouse)
        self.__angle = self.get_angle()
        self.__vel = 10  # velocidade
        self.__image = pg.Surface(self.__size)
        self.__image.fill(RED)
        self.__rect = self.__image.get_rect()
        self.__rect.center = pos

    def get_angle(self):

        # recebe coordenadas relativas entre mouse e player e adiciona erro de recuo
        c_y = (self.__mouse.y - self.__pos.y) + random.randint(-3, 3)
        c_x = (self.__mouse.x - self.__pos.x) + random.randint(-3, 3)

        recoil = random.randint(-3, 3)
        # calcula a hipotenusa, ou arctangente, da tragetoria do lazer
        angle = math.atan2(c_y, c_x)

        return angle

    @ property
    def damage(self):
        return self.__damage

    @ property
    def shooter(self):
        return self.__shooter

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
    def angle(self):
        return self.__angle
