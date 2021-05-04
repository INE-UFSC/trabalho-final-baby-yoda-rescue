import pygame as pg
import random
from jogador import Jogador
from configs import *
from level import Level
from camera import Camera


class Jogo:
    def __init__(self):
        # configs
        self.__FPS = FPS
        self.__caption = TITULO
        self.__sprites = pg.sprite.Group()
        self.__jogador = Jogador()
        self.__level = Level(world)
        self.__camera = Camera(self.__jogador, self.__level)

        self.__background = pg.image.load("data/teste.png")
        self.__bg_x = 0


        # inicializa a janela do pygame
        pg.init()
        # inicializa o audio
        pg.mixer.init()
        # define o titulo
        pg.display.set_caption(self.__caption)
        # define o clock
        self.__clock = pg.time.Clock()
        # adiciona sprites ao grupo sprites - pode ir para fase LOAD
        self.__sprites.add(
            self.__jogador, self.__level.platforms, self.__level.items, self.__level.exit)
        self.__screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.__running = True

    def run(self):
        self.__running = True
        while self.__running:
            # sincroniza o loop com o clock
            self.__clock.tick(self.__FPS)

            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()

    def events(self):
        # eventos
        for event in pg.event.get():
            # se fecha a janela termina o programa
            if event.type == pg.QUIT:
                self.__running = False

    def update(self):

        # Logica de colisão
        # platformas
        # Codigo de controlado_jogo

        # impede o crossmap para a esquerda
        if self.__jogador.pos.x - (self.__jogador.size[0]/2) < 0:
            self.__jogador.pos.x = 0 + (self.__jogador.size[0]/2)

        hits_platform = pg.sprite.spritecollide(
            self.jogador, self.level.platforms, False)
        
        if hits_platform:
            # Percorre a lista de objetos que colidiram com o Player:
            for n in range(0, len(hits_platform)):

                # Prints de teste para colisão em Y:
                #print('self.__jogador.rect.bottom: ', self.__jogador.rect.bottom)
                #print('hits_platform[0].rect.top: ', hits_platform[n].rect.top)
                #print('self.__jogador.rect.top: ', self.__jogador.rect.top)
                #print('hits_platform[0].rect.bottom: ', hits_platform[n].rect.bottom)

                # Colisão No eixo Y:
                #if abs((self.__jogador.rect.bottom -1) - hits_platform[n].rect.top) < \
                #abs(hits_platform[n].rect.bottom - self.__jogador.rect.top) and self.__jogador.vel.y > 0:
                if abs((self.__jogador.rect.bottom -1) - hits_platform[n].rect.top) < 10.5 and self.__jogador.vel.y > 0:
                    #print(f'{n} - SUPERIOR - {abs(self.__jogador.rect.bottom - hits_platform[n].rect.top)}')
                    #print('self.__jogador.vel.y: ',self.__jogador.vel.y)
                    self.__jogador.vel.y = 0
                    self.__jogador.pos.y = hits_platform[n].rect.top + 1
                    self.__jogador.colisions['bottom'] = True

                #elif self.__jogador.rect.bottom > hits_platform[n].rect.bottom and abs(self.__jogador.rect.top - hits_platform[n].rect.bottom) < \
                #abs(self.__jogador.rect.bottom - hits_platform[n].rect.top) and self.__jogador.vel.y < 0:
                elif abs(self.__jogador.rect.top - hits_platform[n].rect.bottom) < 10.5 and self.__jogador.vel.y < 0:
                    #print(f'{n} - INFERIOR - {abs(self.__jogador.rect.top - hits_platform[n].rect.bottom)}')
                    self.__jogador.vel.y = 0
                    self.__jogador.pos.y = hits_platform[n].rect.bottom + \
                    self.__jogador.size[1] - 1
                    self.__jogador.colisions['top'] = True

                # Prints de teste para colisão em X:
                #print('self.__jogador.rect.left: ', self.__jogador.rect.left)
                #print('hits_platform[0].rect.right: ', hits_platform[0].rect.right)
                #print('self.__jogador.rect.right: ', self.__jogador.rect.right)
                #print('hits_platform[0].rect.left: ', hits_platform[0].rect.left)

                # Colisão No eixo X:
                #elif self.__jogador.vel.y != - 13.5 and abs(self.__jogador.rect.left - hits_platform[n].rect.right) < \
                #abs(self.__jogador.rect.right - hits_platform[n].rect.left) and self.__jogador.vel.x < 0:
                elif self.__jogador.vel.y != self.__jogador.jump_acc + self.__jogador.gravidade and \
                    abs(self.__jogador.rect.left - hits_platform[n].rect.right) < 5 and self.__jogador.vel.x < 0:
                    #print(f'{n} - DIREITA - {abs(self.__jogador.rect.left - hits_platform[n].rect.right)}')
                    self.__jogador.vel.x = 0
                    self.__jogador.pos.x = hits_platform[n].rect.right + (self.__jogador.size[0]//2) - 1
                    self.__jogador.colisions['left'] = True
                    print('self.jogador.colisions: ', self.__jogador.colisions)

                elif self.__jogador.vel.y != self.__jogador.jump_acc + self.__jogador.gravidade and \
                    abs(self.__jogador.rect.right - hits_platform[n].rect.left) < 5 and self.__jogador.vel.x > 0:
                    #print(f'{n} - ESQUERDA - {abs(self.__jogador.rect.right - hits_platform[n].rect.left)}')
                    self.__jogador.vel.x = 0
                    self.__jogador.pos.x = hits_platform[n].rect.left - (self.__jogador.size[0]//2) + 1
                    self.__jogador.colisions['right'] = True
                    print('self.jogador.colisions: ',self.__jogador.colisions)
                
                self.__jogador.plat_collide = True

        else:
            self.__jogador.plat_collide = False
            self.__jogador.colisions = {'top': False, 'bottom': False, 'left': False, 'right': False}

        #Colisão com ítens:
        hits_items = pg.sprite.spritecollide(
            self.jogador, self.level.items, True)
        if hits_items:
             self.__jogador.key = True
             print('self.__jogador.key:', self.__jogador.key)

        #Colisão com a saída:
        hits_exit = pg.sprite.spritecollide(
            self.jogador, self.level.exit, False)
        if hits_exit and self.__jogador.key == True:
            print('Você conseguiu!')
            jogo.quit()
            #pg.quit()





        self.__sprites.update()
        #self.__camera.update()

    def draw(self):
        #lógica de replicação e movimento do background
        self.__rel_x = self.__bg_x % self.__background.get_rect().width
        self.__screen.blit(self.__background, [self.__rel_x - self.__background.get_rect().width,0])
        if self.__rel_x < WIDTH:
            self.__screen.blit(self.__background, (self.__rel_x, 0))
        self.__bg_x -= 1

        self.__sprites.draw(self.__screen)
        # realiza o flip apos desenhar tudo
        pg.display.flip()

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, new_value):
        self.__running = new_value

    @property
    def clock(self):
        return self.__clock

    @property
    def jogador(self):
        return self.__jogador

    @property
    def level(self):
        return self.__level
