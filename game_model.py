from player import Player
from enemy import Enemy
from level import Level
from lazer import Lazer
from configs import *

class GameModel:
    def __init__(self):
        self.__FPS = FPS
        self.__player = Player(dicionario["player"])
        # implementando apenas um nivel
        self.__level = Level(world)
        self.__enemies = []

        '''for i in range(30):
            self.__enemies.append(Enemy(dicionario["enemy"]))'''

    @property
    def FPS(self):
        return self.__FPS

    @property
    def player(self):
        return self.__player

    @property
    def level(self):
        return self.__level

    def gen_lazer(self, shooter, pos, mouse):
        return Lazer(shooter, pos, mouse)
