#Imports, adicionar os imports das clases
import pygame, sys
from pygame.locals import * # pygame.locals para não ter que chamar sempre .locals.func
import random, time

#Iniciando o pygame :
pygame.init()
# Dimensões da janela do pygame
WIDTH = 800
HEIGHT = 600
FPS = 60 # Framerate máximo;
FramePerSec = pygame.time.Clock() # Cada frame corresponde a um clock do jogo, assim a cada segundo 60 verificações

# Acho que a definição dessa variáveis devem ficar em fase
vec = pygame.math.Vector2 #2 for two dimensional
ACC = 0.5 # Aceleração
FRIC = -0.12 # Atrito

# inicia a janela do pygame:
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

#metodo de iniciar o jogo a partir da classe fase e dos inputs do número da fase





                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)