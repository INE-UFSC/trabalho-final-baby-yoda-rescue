from abc import ABC, abstractmethod

class CamScroll(ABC):
    def __init__(self, camera, jogador):
        self.__camera = camera
        self.__jogador = jogador

    @abstractmethod
    def camera(self):
        return self.__camera

    @abstractmethod
    def jogador(self):
        return self.__jogador

    @abstractmethod
    def scroll(self):
        pass