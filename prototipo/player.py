import pygame
import glob

'''
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center = (160, 520))
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
'''

class Player(pygame.sprite.Sprite):
    def __init__(self, nome, action, *groups): #Passa os parâmetros (atributos) da classe, incluindo a direção da animação do sprite
        super().__init__()
        self.__nome = nome
        self.__action = action

        self.image = pygame.Surface((32, 48))
        self.rect = self.image.get_rect()

        '''
        FUTURA MOVIMENTAÇÃO, TALVEZ?
        
        self.pos = vec((int(WIDTH / 2), 0))  # SPAWN POINT
        self.vel = vec(0, 0)  # Velocidade no momento do spawn x,y
        self.acc = vec(0, 0)
        '''

        #ANIMAÇÃO - Deverá ser colocada na classe Personagem
        list_img = glob.glob(f"data\\{self.__action}*.png") #Lista de imagens que armazena os movimemtos do sprite de acordo com seu nome (parâmetro action)
        len_img1 = len(list_img[0]) #Variável que armazena o tamanho da primeira imagem
        self.images = [pygame.image.load(img) for img in list_img if len_img1 == len(img)] #Self.images carrega o sprite da lista se ele for igual ao primeiro sprite
        self.images.extend([pygame.image.load(img) for img in list_img if len(img) > len_img1]) #Carrega todos os sprites posteriores ao primeiro que existirem
        self.index = 0 #Posição inicia em 0

    def update(self, *args):
        #ANIMAÇÃO - Deverá ser colocada na classe Personagem
        self.image = self.images[self.index] #Sprite atual recebe o sprite da posição self.index, que inicia em 0
        self.index += 1 #Aí o self.index vai incrementando e trocando o sprite da lista
        if self.index >= len(self.images): #Até que ele chegue ao seu tamanho máximo
            self.index = 0 #Quando chega, index = 0 para reiniciar a animação

        '''
        FUTURA MOVIMENTAÇÃO, COLISÃO

        hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.vel.y > 0:
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1
        '''

    def move(self, action):
        self.__action = action
        if self.__action == "mando-esquerda":
            self.rect.x -= 2
        elif self.__action == "mando-direita":
            self.rect.x += 2
 
    def jump(self):
        '''
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
           self.vel.y = -15
        '''



