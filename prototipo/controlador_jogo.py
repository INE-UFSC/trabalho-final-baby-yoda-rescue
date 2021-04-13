import pygame, sys
from pygame.locals import *

pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional

# Classes para desenhar:
class Player(pygame.sprite.Sprite): #Desenha um player
    def __init__(self, name: str, size: tuple, color: tuple, spawn: tuple):
        super().__init__() 
        self.name = name
        self.size = size
        self.color = color
        self.spawn = spawn
        #self.image = pygame.image.load("character.png")
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.pos = vec(spawn)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False
        
    def move(self):
        self.acc = vec(0,0.5) # a aceleração continua em 0.5 é o que define a gravidade para o player no jogo
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
                 
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
         
        if self.pos.x + (self.size[0]/2) > WIDTH:
            self.pos.x = WIDTH - (self.size[0]/2) # Impede o crossmap para direita
        if self.pos.x - (self.size[0]/2) < 0:
            self.pos.x = 0 + (self.size[0]/2) # impede o crossmap para a esquerda
             
        self.rect.midbottom = self.pos
 
    def jump(self): 
        hits = pygame.sprite.spritecollide(self, platforms, False) # último padrão é o kill, habilitar em plataformas armadilhas
        if hits and not self.jumping:
           self.jumping = True
           self.vel.y = -13
        hits = pygame.sprite.spritecollide(self, walls, False) # Essas plataformas possuem um bug, fico preso e não consigo me reposicionar sobre elas
        if hits and not self.jumping:
           self.jumping = True
           self.vel.y = -13
 
    def update(self):
        print(f'X:{int((self.pos.x*10)//10)}Y:{int((self.pos.y*10)//10)}')
        hits_plataforms = pygame.sprite.spritecollide(self, platforms, False)
        if self.vel.y > 0:        
            if hits_plataforms:
                if self.pos.y < hits_plataforms[0].rect.bottom:               
                    self.pos.y = hits_plataforms[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False
                #print(hits_plataforms[0].rect.bottom)

        hits_walls = pygame.sprite.spritecollide(self, walls, False)
        if self.vel.y > 0:        
            if hits_walls:
                if self.pos.y > hits_walls[0].rect.bottom:               
                    self.pos.y = hits_walls[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False
                #print(hits_walls[0].rect.bottom)
        if self.vel.x > 0:
            if hits_walls:
                print(f'self.pos.x RIGHT = {hits_walls[0].rect.right}')
                if self.pos.x < (hits_walls[0].rect.right):
                    self.pos.x = hits_walls[0].rect.right - (self.size[0])
                    self.vel.x = 0
        if self.vel.x < 0:
            if hits_walls:
                print(f'self.pos.x LEFT = {hits_walls[0].rect.left}')
                if self.pos.x > (hits_walls[0].rect.left):        
                    self.pos.x = (hits_walls[0].rect.left) + (self.size[0])
                    self.vel.x = 0
# Esse código também funciona, talvez seja útil quando houver mais plataformas      
'''hits_walls = pygame.sprite.spritecollide(self, walls, False)
        if self.vel.y > 0:        
            if hits_walls:
                if self.pos.y > hits_walls[0].rect.bottom:               
                    self.pos.y = hits_walls[0].rect.top -1
                    self.vel.y = 0
                    self.jumping = False
                #print(hits_walls[0].rect.bottom)
        if self.vel.x > 0:
            if hits_walls:
                print(f'self.pos.x TOP_RIGHT = {hits_walls[0].rect.topright}')
                if self.pos.x < (hits_walls[0].rect.topright)[0]:
                    self.pos.x = (hits_walls[0].rect.topright)[0] - (self.size[0])
                    self.vel.x = 0
        if self.vel.x < 0:
            if hits_walls:
                print(f'self.pos.x TOP_LEFT = {hits_walls[0].rect.topleft}')
                if self.pos.x > (hits_walls[0].rect.topright)[0]:        
                    self.pos.x = (hits_walls[0].rect.topleft)[0] + (self.size[0])
                    self.vel.x = 0'''


class Platform(pygame.sprite.Sprite):
    def __init__(self, name: str, size: tuple, color: tuple, spawn: tuple):
        super().__init__()
        self.name = name
        self.size = size
        self.color = color
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center = (spawn))
        
    def move(self):
        pass

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
PURPLE = (148, 0, 211)

FPS = 60
HEIGHT, WIDTH = 600, 800 # Dimensões da tela
ACC, FRIC = 0.5, -0.12 # Aceleração e Atrito

FramePerSec = pygame.time.Clock() 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grupo 5 - Protótipo do Jogo")


mando = Player('Mando', (35, 52), (WHITE), (WIDTH/WIDTH, HEIGHT - 20))
floor = Platform('floor', (WIDTH, 20), (RED), (WIDTH/2, HEIGHT - 10) ) 
plat1 = Platform('platform1', (WIDTH/5, 20), (RED), (WIDTH/4, HEIGHT* 0.75 -20))
plat2 = Platform('platform1', (WIDTH/5, 20), (RED), (WIDTH/4, HEIGHT* 0.50 -20))
plat3 = Platform('platform1', (WIDTH/5, 20), (RED), (WIDTH/4, HEIGHT* 0.25 -20))
wall1 = Platform('wall1', (20, HEIGHT*0.75 + 10), (BLUE), (WIDTH/4 + (WIDTH/5)/2, HEIGHT/2 + 50))

P1 = mando #Define o player1 dessa fase
level_plataforms = floor, plat1, plat2, plat3 #Define as plataformas que compõem essa fase
level_walls = wall1 #Define as Paredes intransponíveis da fase

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, level_plataforms, level_walls)
 
platforms = pygame.sprite.Group()
platforms.add(level_plataforms)

walls = pygame.sprite.Group()
walls.add(level_walls)

# Loop do jogo:
while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump()
         
    displaysurface.fill((255,0,255))
    P1.update()
 
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()
 
    pygame.display.update()
    FramePerSec.tick(FPS)
