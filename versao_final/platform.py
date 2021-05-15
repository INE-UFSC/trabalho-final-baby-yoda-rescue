from configs import *

class Platform(pg.sprite.Sprite):
    def __init__(self, x: int, y: int, w: int, h: int, img):
        super().__init__()
        self.__image = pg.transform.scale(img,(TILE_SIZE_W, TILE_SIZE_H))
        self.__rect = self.__image.get_rect()
        self.__rect.x = x
        self.__rect.y = y

    @property
    def rect(self):
        return self.__rect

    @property
    def image(self):
        return self.__image
