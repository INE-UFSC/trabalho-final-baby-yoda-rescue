import pygame as pg
import random
from game_model import GameModel
from game_view import GameView
import math

# função para testar as colisões


def colision_test(rect, tiles):
    hits_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hits_list.append(tile)
    return hits_list

# função para movimentos


def move(rect, movement, tiles):  # quem se move, movimento, com quem pode se colidir
    # dicionário pra saber com que lado se colidiu
    collision_types = {'top': False, 'bottom': False,
                       'right': False, 'left': False}
    # Movimento em X:
    rect.x += movement[0]
    hit_list = colision_test(rect, tiles)  # tile vai ser a classe dos blocos
    for tile in hit_list:
        if movement[0] > 0:  # ou seja se movendo para a direita
            rect.right = tile.rect.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.rect.right
            collision_types['left'] = True
    # Movimento em Y:
    rect.y += movement[1]
    hit_list = colision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:  # ou seja se movendo para a direita
            rect.bottom = tile.rect.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.rect.bottom
            collision_types['top'] = True
    return rect, collision_types


class GameController:
    def __init__(self):
        self.__model = GameModel()
        self.__sprites = pg.sprite.Group()
        self.__attacks = pg.sprite.Group()
        self.__view = GameView(self.__model.player,
                               self.__model.level,
                               self.__sprites,
                               self.__attacks)
        self.__player = self.__model.player
        self.__level = self.__model.level
        self.__clock = pg.time.Clock()
        # inicializa os modulos do pygame e retorna uma tupla com resultados
        self.__modules = pg.init()
        self.__running = True

    def load_level(self):
        # posicao do jogador, deve ser carregada de level
        self.__player.pos = self.__level.spawn_point

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

            self.commands(event)

    def update(self):
        self.physics()
        self.balistics()
        self.collisions()

    def physics(self):

        # Updates do player:
        self.__player.acc = self.__player.vec(
            0, 0.5)  # Segundo parâmetro para gravidade
        self.__player.acc.x += self.__player.vel.x * self.__player.fric
        self.__player.vel += self.__player.acc
        self.__player.pos += self.__player.vel + \
            self.__player.std_acc * self.__player.acc

    def balistics(self):
        for lazer in self.__attacks.sprites():
            lazer.pos.x += math.cos(lazer.angle) * lazer.vel
            lazer.pos.y += math.sin(lazer.angle) * lazer.vel
            lazer.rect.center = lazer.pos

    def collisions(self):

        # Colisão de Player com plataformas
        collision_types = move(
            self.__player.rect, self.__player.vel, self.__level.platforms.sprites())

        print(self.__player.pos)
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

    def commands(self, event):
        # Posição do player marcada como ponto do meio inferior
        self.__player.rect.midbottom = self.__player.pos

        # logica de comandos
        keys = pg.key.get_pressed()

        # seta esquerda
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.__player.acc.x = -1 * self.__player.std_acc

        # seta direita
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.__player.acc.x = self.__player.std_acc

        # espaco
        if keys[pg.K_SPACE] or keys[pg.K_w]:
            self.__player.vel.y = self.__player.jump_acc

        # clique de mouse mais posicao
        if event.type == pg.MOUSEBUTTONDOWN:
            lazer = self.__model.gen_lazer(
                self.__player.rect.center, pg.mouse.get_pos())
            self.__attacks.add(lazer)
            self.__view.update_attacks()

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, new_value):
        self.__running = new_value

    @property
    def sprites(self):
        return self.__sprites
