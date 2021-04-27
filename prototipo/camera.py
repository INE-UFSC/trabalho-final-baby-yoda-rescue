import pygame as pg
from pygame import *
from configs import *

vec = pg.math.Vector2


class CameraAwareLayeredUpdates(pg.sprite.LayeredUpdates):
    def __init__(self, target):
        super().__init__()
        self.__target = target #personagem
        self.__cam = vec(0, 0)
        if self.__target:
            self.add(target)

    def update(self, *args):
        super().update(*args)
        if self.__target:
            x = -self.__target.rect.center[0] + WIDTH/2
            y = -self.__target.rect.center[1] + HEIGHT/2
            self.__cam += (vec((x, y)) - self.__cam) * 0.05
            self.__cam.x = max(-(WIDTH/2), min(0, self.__cam.x))
            self.__cam.y = max(-(HEIGHT/2), min(0, self.__cam.y))

    def draw(self, surface):
        spritedict = self.spritedict
        surface_blit = surface.blit
        dirty = self.lostsprites
        self.lostsprites = []
        dirty_append = dirty.append
        init_rect = self._init_rect
        for spr in self.sprites():
            rec = spritedict[spr]
            newrect = surface_blit(spr.image, spr.rect.move(self.__cam))
            if rec is init_rect:
                dirty_append(newrect)
            else:
                if newrect.colliderect(rec):
                    dirty_append(newrect.union(rec))
                else:
                    dirty_append(newrect)
                    dirty_append(rec)
            spritedict[spr] = newrect
        return dirty  