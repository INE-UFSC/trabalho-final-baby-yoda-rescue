import pygame
import random

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((42, 70))
        #self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40), 0))

      def move(self):
