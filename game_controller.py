import pygame as pg
import random
from game_model import GameModel
from game_view import GameView


class GameController:
    def __init__(self):
        self.__model = GameModel()
        self.__view = GameView(self.__model.player, self.__model.level)
        self.__player = self.__model.player
        self.__level = self.__model.level
        self.__clock = pg.time.Clock()

    def run(self):
        self.__running = True
        while self.__running:
            # sincroniza o loop de eventos com o clock
            self.__clock.tick(self.__model.FPS)

            self.events()
            self.update()
            self.__view.draw()

    # funcao de saida do pygame chamada em caso de fechamento de janela
    def quit(self):
        pg.quit()

    # events listener
    def events(self):
        for event in pg.event.get():
            # se fecha a janela termina o programa
            if event.type == pg.QUIT:
                self.__running = False

    def update(self):
        # impede o crossmap para a esquerda
        if self.__player.pos.x - (self.__player.size[0]/2) < 0:
            self.__player.pos.x = 0 + (self.__player.size[0]/2)

        hits_platform = pg.sprite.spritecollide(
            self.__player, self.__level.platforms, False)

        if hits_platform:
            # Percorre a lista de objetos que colidiram com o Player:
            for n in range(0, len(hits_platform)):

                # Prints de teste para colisão em Y:
                #print('self.__player.rect.bottom: ', self.__player.rect.bottom)
                #print('hits_platform[0].rect.top: ', hits_platform[n].rect.top)
                #print('self.__player.rect.top: ', self.__player.rect.top)
                #print('hits_platform[0].rect.bottom: ', hits_platform[n].rect.bottom)

                # Colisão No eixo Y:
                # if abs((self.__player.rect.bottom -1) - hits_platform[n].rect.top) < \
                # abs(hits_platform[n].rect.bottom - self.__player.rect.top) and self.__player.vel.y > 0:
                if abs((self.__player.rect.bottom - 1) - hits_platform[n].rect.top) < 10.5 and self.__player.vel.y > 0:
                    #print(f'{n} - SUPERIOR - {abs(self.__player.rect.bottom - hits_platform[n].rect.top)}')
                    #print('self.__player.vel.y: ',self.__player.vel.y)
                    self.__player.vel.y = 0
                    self.__player.pos.y = hits_platform[n].rect.top + 1
                    self.__player.colisions['bottom'] = True

                # elif self.__player.rect.bottom > hits_platform[n].rect.bottom and abs(self.__player.rect.top - hits_platform[n].rect.bottom) < \
                # abs(self.__player.rect.bottom - hits_platform[n].rect.top) and self.__player.vel.y < 0:
                if abs(self.__player.rect.top - hits_platform[n].rect.bottom) < 10.5 and self.__player.vel.y < 0:
                    #print(f'{n} - INFERIOR - {abs(self.__player.rect.top - hits_platform[n].rect.bottom)}')
                    self.__player.vel.y = 0
                    self.__player.pos.y = hits_platform[n].rect.bottom + \
                        self.__player.size[1] - 1
                    self.__player.colisions['top'] = True

                # Prints de teste para colisão em X:
                #print('self.__player.rect.left: ', self.__player.rect.left)
                #print('hits_platform[0].rect.right: ', hits_platform[0].rect.right)
                #print('self.__player.rect.right: ', self.__player.rect.right)
                #print('hits_platform[0].rect.left: ', hits_platform[0].rect.left)

                # Colisão No eixo X:
                # elif self.__player.vel.y != - 13.5 and abs(self.__player.rect.left - hits_platform[n].rect.right) < \
                # abs(self.__player.rect.right - hits_platform[n].rect.left) and self.__player.vel.x < 0:
                if self.__player.vel.y != self.__player.jump_acc + self.__player.gravidade and \
                        abs(self.__player.rect.left - hits_platform[n].rect.right) < 5 and self.__player.vel.x < 0:
                    #print(f'{n} - DIREITA - {abs(self.__player.rect.left - hits_platform[n].rect.right)}')
                    self.__player.vel.x = 0
                    self.__player.pos.x = hits_platform[n].rect.right + (
                        self.__player.size[0]//2) - 1
                    self.__player.colisions['left'] = True
                    print('self.player.colisions: ', self.__player.colisions)

                if self.__player.vel.y != self.__player.jump_acc + self.__player.gravidade and \
                        abs(self.__player.rect.right - hits_platform[n].rect.left) < 5 and self.__player.vel.x > 0:
                    #print(f'{n} - ESQUERDA - {abs(self.__player.rect.right - hits_platform[n].rect.left)}')
                    self.__player.vel.x = 0
                    self.__player.pos.x = hits_platform[n].rect.left - (
                        self.__player.size[0]//2) + 1
                    self.__player.colisions['right'] = True
                    print('self.player.colisions: ', self.__player.colisions)

                self.__player.plat_collide = True

        else:
            self.__player.plat_collide = False
            self.__player.colisions = {
                'top': False, 'bottom': False, 'left': False, 'right': False}

        # Colisao com itens:
        hits_items = pg.sprite.spritecollide(
            self.player, self.level.items, True)
        if hits_items:
            self.__player.key = True
            print('self.__player.key:', self.__player.key)

        # Colisao com a saida:
        hits_exit = pg.sprite.spritecollide(
            self.player, self.level.exit, False)
        if hits_exit and self.__player.key == True:
            print('Você conseguiu!')
            jogo.quit()
            # pg.quit()

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, new_value):
        self.__running = new_value
