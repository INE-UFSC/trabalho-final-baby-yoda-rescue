from configs import *

class Camera():
    def __init__(self, jogador, level):
        super().__init__() #Fazer abstract
        self.__jogador = jogador
        self.__level = level

    def update(self):
        #Lógica para direita e esquerda
        #Problema: plataformas se juntam na esquerda, mas não se juntam na direita (por quê?)
        if self.__jogador.rect.right > WIDTH / 2:
            self.__jogador.pos.x -= abs(self.__jogador.vel.x) #centraliza o jogador
            for platf in self.__level.platforms:
                if not self.__jogador.colisions['right']:
                    platf.rect.x -= abs(self.__jogador.vel.x) #movimenta plataforma na direção oposta
        elif self.__jogador.rect.left < WIDTH / 2:
            self.__jogador.pos.x += abs(self.__jogador.vel.x)
            for platf in self.__level.platforms:
                if not self.__jogador.colisions['left']:
                    platf.rect.x += abs(self.__jogador.vel.x)
        
        #Lógica para cima e para baixo
        #Problema: jogador inesperadamente cai da plataforma vermelha, sem razão aparente
        if self.__jogador.rect.top <= HEIGHT / 4:
            self.__jogador.pos.y += abs(self.__jogador.vel.y)
            for platf in self.__level.platforms:
                if not self.__jogador.colisions['top']:
                    platf.rect.y += abs(self.__jogador.vel.y)
        elif self.__jogador.rect.bottom > HEIGHT * 3/4:
            self.__jogador.pos.y -= abs(self.__jogador.vel.y)
            for platf in self.__level.platforms:
                if not self.__jogador.colisions['bottom']:
                    platf.rect.y -= abs(self.__jogador.vel.y)
