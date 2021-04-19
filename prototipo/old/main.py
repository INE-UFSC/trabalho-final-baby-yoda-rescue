import pygame, sys
import random, time
from pygame.locals import * #pygame.locals para não ter que chamar sempre .locals.func
#from enemy import Enemy
from player import Player

#Iniciando o pygame
pygame.init()

#Dimensões da janela do pygame
WIDTH = 800
HEIGHT = 600
FPS = 60 #Framerate máximo
FramePerSec = pygame.time.Clock() #Cada frame corresponde a um clock do jogo, assim a cada segundo 60 verificações

#Inicia a janela do pygame:
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Protótipo do Jogo - Grupo 5") #Define o nome do jogo na janela

#metodo de iniciar o jogo a partir da classe fase e dos inputs do número da fase

#Criando objetos
player_mando = Player("Mando", "mando-idle")
#E1 = Enemy()

#Criando Grupos de Sprites
enemies = pygame.sprite.Group()
player = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

player.add(player_mando)
all_sprites.add(player)

background = pygame.Surface((WIDTH, HEIGHT))
background.fill((207,236,207))
#background.rect = background.get_rect()


if __name__ == "__main__":
    #Game Loop
    while True:
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break

        SCREEN.blit(background, (0,0))
        
        #Moves and Re-draws all Sprites
        for entity in all_sprites:
            SCREEN.blit(entity.image, entity.rect)
            if pressed_keys[pygame.K_LEFT]:
                action = "mando-esquerda"
            elif pressed_keys[pygame.K_RIGHT]:
                action = "mando-direita"
            else:
                action = "mando-idle"
            entity.move(action)

        all_sprites.update()
        all_sprites.draw(SCREEN)
        player.update()
        player.draw(SCREEN)
        enemies.update()
        enemies.draw(SCREEN)

        FramePerSec.tick(FPS)
        pygame.display.update()
