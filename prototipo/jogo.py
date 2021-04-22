import pygame as pg
import random
from jogador import Jogador
from configs import *
from level import Level


class Jogo:
    def __init__(self):
        # configs
        self.__FPS = FPS
        self.__caption = TITULO
        self.__sprites = pg.sprite.Group()
        self.__jogador = Jogador()
        self.__level = Level()

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
            self.__jogador, self.__level.platforms)
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

        hits_platform = pg.sprite.spritecollide(self.jogador, self.level.platforms, False)
        if hits_platform:
            for n in range(0, len(hits_platform)):
                
                #Prints de teste para colisão em Y:
                #print('self.__jogador.rect.bottom: ', self.__jogador.rect.bottom)
                #print('hits_platform[0].rect.top: ', hits_platform[0].rect.top)
                #print('self.__jogador.rect.top: ', self.__jogador.rect.top)
                #print('hits_platform[0].rect.bottom: ', hits_platform[0].rect.bottom)
                # Colisão No eixo Y:
                if abs(self.__jogador.rect.bottom - hits_platform[n].rect.top) < \
                abs(hits_platform[n].rect.bottom - self.__jogador.rect.top) and self.__jogador.vel.y > 0:
                        print(f'{n} - SUPERIOR - {abs(self.__jogador.rect.bottom - hits_platform[n].rect.top)}')
                        self.__jogador.vel.y = 0
                        self.__jogador.pos.y = hits_platform[n].rect.top +1
                        
                elif abs(self.__jogador.rect.top - hits_platform[n].rect.bottom) < \
                abs(self.__jogador.rect.bottom - hits_platform[n].rect.top) and self.__jogador.vel.y < 0:
                        print(f'{n} - INFERIOR - {abs(self.__jogador.rect.top - hits_platform[n].rect.bottom)}')
                        self.__jogador.vel.y = 0
                        self.__jogador.pos.y = hits_platform[n].rect.bottom + self.__jogador.size[1] -1
                        
                #Prints de teste para colisão em X:
                #print('self.__jogador.rect.left: ', self.__jogador.rect.left)
                #print('hits_platform[0].rect.right: ', hits_platform[0].rect.right)
                #print('self.__jogador.rect.right: ', self.__jogador.rect.right)
                #print('hits_platform[0].rect.left: ', hits_platform[0].rect.left)
                # Colisão No eixo X:
                
                elif abs(self.__jogador.rect.left - hits_platform[n].rect.right) < \
                     abs(self.__jogador.rect.right - hits_platform[n].rect.left) and self.__jogador.vel.x < 0:
                        print(f'{n} - DIREITA - {abs(self.__jogador.rect.left - hits_platform[n].rect.right)}')
                        self.__jogador.vel.x = 0
                        self.__jogador.pos.x = hits_platform[n].rect.right + (self.__jogador.size[0]//2) -1
                        
                elif abs(self.__jogador.rect.right - hits_platform[n].rect.left) < \
                     abs(self.__jogador.rect.left - hits_platform[n].rect.right) and self.__jogador.vel.x > 0:
                        print(f'{n} - ESQUERDA - {abs(self.__jogador.rect.right - hits_platform[n].rect.left)}')
                        self.__jogador.vel.x = 0
                        self.__jogador.pos.x = hits_platform[n].rect.left - (self.__jogador.size[0]//2) +1
                
                self.__jogador.plat_collide = True
     
        else:
            self.__jogador.plat_collide = False
            
        self.__sprites.update()

    def draw(self):
        self.__screen.fill(BLACK)
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
