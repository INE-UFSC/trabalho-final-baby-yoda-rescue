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
        self.__tupx = 0
        self.__tupy = 0

        self.__SAVE_DATA = {"level": [self.__level.current, self.__level.index],
                            # ,
                            "player": [self.__player.health, self.__player.key, self.__player.pos.x, self.__player.pos.y]
                            # "enemy": self.__level.enemies
                            }

    #health, position, key, tilemap

    def data(self, save=False):
        if save:
            self.__SAVE_DATA["player"][0] = self.__player.health
            self.__SAVE_DATA["player"][1] = self.__player.key
            self.__SAVE_DATA["player"][2] = self.__player.pos[0]
            self.__SAVE_DATA["player"][3] = self.__player.pos[1]
            self.__SAVE_DATA["level"][0] = self.__level.current
            self.__SAVE_DATA["level"][1] = self.__level.index
            #self.__SAVE_DATA["enemy"] = self.__level.enemies
            with open("SAVE_DATA.txt", "w") as data_file:
                json.dump(self.__SAVE_DATA, data_file)
        else:
            with open("SAVE_DATA.txt") as data_file:
                self.__SAVE_DATA = json.load(data_file)
            self.__player.health = self.__SAVE_DATA["player"][0]
            self.__player.key = self.__SAVE_DATA["player"][1]
            self.__tupx = self.__SAVE_DATA["player"][2]
            self.__tupy = self.__SAVE_DATA["player"][3]
            self.__player.pos = vec(self.__tupx, self.__tupy)
            self.__level.current = self.__SAVE_DATA["level"][0]
            self.__level.index = self.__SAVE_DATA["level"][1]
            self.__level.world = self.__level.current

    @property
    def FPS(self):
        return self.__FPS

    @property
    def player(self):
        return self.__player

    @property
    def level(self):
        return self.__level

    def gen_lazer(self, shooter, mouse):
        return Lazer(shooter, mouse)
