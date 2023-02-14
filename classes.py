import json
import pygame
import variaveis
import random
from constantes import*


SURFACE_COLOR = (167, 255, 100)

   



class Estrela(pygame.sprite.Sprite):
        '''Classe para criar pássaros'''
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50,50))
            self.image.fill(RED)
          
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH/2
            self.rect.centery = HEIGHT - 50

            
            
          
            
        def update(self):
            '''Método para atualizar a posição dos pássaros e trocar as imagens dos pássaros para dar animação'''
            pass



class Alvo(pygame.sprite.Sprite):
        '''Classe para criar pássaros'''
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((20,20))
            self.image.fill(RED)
          
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH/2
            self.rect.centery = 50

            
            
          
            
        def update(self):
            '''Método para atualizar a posição dos pássaros e trocar as imagens dos pássaros para dar animação'''
            pass