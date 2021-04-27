from .camscroll import CamScroll

class Follow(CamScroll):
    def __init__(self, camera, jogador):
        CamScroll.__init__(self, camera, jogador)
        self.__camera = camera
        self.__jogador = jogador

    def scroll(self):
        self.__camera.offset_float.x += (self.__jogador.rect.x - self.__camera.offset_float.x + self.__camera.CONST.x)
        self.__camera.offset_float.y += (self.__jogador.rect.y - self.__camera.offset_float.y + self.__camera.CONST.y)
        self.__camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)