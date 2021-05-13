from configs import *

# Deveria ser subclasse de item, mas generalizamos dps:
class Key(pg.sprite.Sprite):
    def __init__(self, x: int, y: int, w: int, h: int, color: tuple):
        super().__init__()
        self.__image = pg.Surface((w, h))
        self.__image.fill(color)
        self.__rect = self.__image.get_rect()
        self.__rect.x = x
        self.__rect.y = y

    @property
    def rect(self):
        return self.__rect

    @property
    def image(self):
        return self.__image
