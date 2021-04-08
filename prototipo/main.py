import pygame, sys
import random, time
from pygame.locals import * #pygame.locals para não ter que chamar sempre .locals.func
#from enemy import Enemy
#from player import Player

#Iniciando o pygame
pygame.init()

#Dimensões da janela do pygame
WIDTH = 800
HEIGHT = 600
FPS = 60 #Framerate máximo
FramePerSec = pygame.time.Clock() #Cada frame corresponde a um clock do jogo, assim a cada segundo 60 verificações

'''
Comentei para ser visto depois

#Acho que a definição dessa variáveis devem ficar em fase
vec = pygame.math.Vector2 #2 for two dimensional
ACC = 0.5 # Aceleração
FRIC = -0.12 # Atrito

'''

#Inicia a janela do pygame:
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game") #Define o nome do jogo na janela

#metodo de iniciar o jogo a partir da classe fase e dos inputs do número da fase

#Criando objetos
'''P1 = Player()
E1 = Enemy()
'''

#Criando Grupos de Sprites
enemies = pygame.sprite.Group()
#enemies.add(E1)

player = pygame.sprite.Group()
#player.add(P1)

all_sprites = pygame.sprite.Group()

background = pygame.Surface((WIDTH, HEIGHT))
background.fill((207,236,207))
#background.rect = background.get_rect()

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

if __name__ == "__main__":
    #Game Loop
    while True:

        #Cycles through all events occuring
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break
            '''   
            if event.type == INC_SPEED:
                  SPEED += 0.5
            '''

        SCREEN.blit(background, (0,0))
        #scores = font_small.render(str(SCORE), True, BLACK)
        #SCREEN.blit(scores, (10,10))

        #Moves and Re-draws all Sprites
        for entity in all_sprites:
            SCREEN.blit(entity.image, entity.rect)
            entity.move()

        all_sprites.update()
        all_sprites.draw(SCREEN)
        player.update()
        player.draw(SCREEN)
        enemies.update()
        enemies.draw(SCREEN)

        #To be run if collision occurs between Player and Enemy
        '''if pygame.sprite.spritecollideany(P1, enemies):
              pygame.mixer.Sound('crash.wav').play()
              time.sleep(1)

              display.fill(RED) #trocar por rgb do vermelho
              display.blit(game_over, (30,250))

              pygame.display.update()
              for entity in all_sprites:
                    entity.kill()
              time.sleep(2)
              pygame.quit()
              sys.exit()
        '''

        FramePerSec.tick(FPS)
        pygame.display.update()
