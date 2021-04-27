from camscroll import CamScroll

class Auto(CamScroll):
    def __init__(self, camera, jogador):
        CamScroll.__init__(self, camera, jogador)

    def scroll(self):
        self.__camera.offset.x += 1