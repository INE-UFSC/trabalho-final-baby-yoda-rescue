import pygame as pg
import random
from game_model import GameModel
from game_view import GameView


class GameController:
    def __init__(self):
        self.__model = GameModel()
        self.__sprites = pg.sprite.Group()
        self.__view = GameView(self.__model.player,
                               self.__model.level, self.__sprites)

        self.__player = self.__model.player
        self.__level = self.__model.level
        self.__clock = pg.time.Clock()
        # inicializa os modulos do pygame e retorna uma tupla com resultados
        self.__modules = pg.init()
        self.__running = True

    def run(self):
        self.load_level()
        while self.__running:
            # sincroniza o loop de eventos com o clock
            self.__clock.tick(self.__model.FPS)
            self.events()
            self.update()
            self.__view.draw()

    # funcao de saida do pygame chamada em caso de fechamento de janela
    def quit(self):
        self.__running = False
        pg.quit()

    def events(self):
        for event in pg.event.get():
            # se fecha a janela termina o programa
            if event.type == pg.QUIT:
                self.quit()

    def update(self):
        self.physics()
        self.collisions()
        self.commands()

    def physics(self):
        # aplica friccao ao eixo x
        self.__player.acc.x += self.__player.vel.x * -0.12

        # equacoes de movimento
        self.__player.vel += self.__player.acc
        self.__player.pos += (self.__player.vel +
                              self.__player.std_acc * self.__player.acc)

    def collisions(self):

        # Colisao com itens:
        hits_items = pg.sprite.spritecollide(
            self.__player, self.__level.items, True)
        if hits_items:
            self.__player.key = True
            print('self.__player.key:', self.__player.key)

        # Colisao com a saida:
        hits_exit = pg.sprite.spritecollide(
            self.__player, self.__level.exit, False)
        if hits_exit and self.__player.key == True:
            self.quit()  # sai do jogo apos conseguir a chave

    def commands(self):
        self.__player.rect.midbottom = self.__player.pos
        # logica de comandos
        keys = pg.key.get_pressed()

        # seta esquerda
        if keys[pg.K_LEFT]:
            self.__player.acc.x = -1 * self.__player.std_acc

        # seta direita
        if keys[pg.K_RIGHT]:
            self.__player.acc.x = self.__player.std_acc

        # espaco
        if keys[pg.K_SPACE]:
            self.__player.vel.y = self.__player.jump_acc

    def load_level(self):
        # posicao do jogador, deve ser carregada de level
        self.__player.pos = self.__level.spawn_point

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, new_value):
        self.__running = new_value

    @property
    def sprites(self):
        return self.__sprites
