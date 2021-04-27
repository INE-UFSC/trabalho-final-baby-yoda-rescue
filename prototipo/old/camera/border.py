from camscroll import CamScroll

class Border(CamScroll):
    def __init__(self, camera, jogador):
        CamScroll.__init__(self, camera, jogador)

    def scroll(self):
        self.__camera.offset_float.x += (self.jogador.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
        self.__camera.offset_float.y += (self.jogador.rect.y - self.camera.offset_float.y + self.camera.CONST.y)
        self.__camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)
        #self.__camera.offset.x = max(self.jogador.left_border, self.camera.offset.x)
        #self.__camera.offset.x = min(self.camera.offset.x, self.jogador.right_border - self.camera.DISPLAY_W)
