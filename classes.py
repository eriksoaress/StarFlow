import json
import pygame
import variaveis
import random
from constantes import*


SURFACE_COLOR = (167, 255, 100)

   



class Estrela(pygame.sprite.Sprite):
        '''Classe para criar a estrela, o objeto que disparará no alvo'''
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("et.png")
            self.image = pygame.transform.scale(self.image, (50,50))
        
           
           
          
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH/2
            self.rect.centery = HEIGHT - 50

            
            
          
            
        def update(self, direita):
            '''Método para atualizar a posição dos pássaros e trocar as imagens dos pássaros para dar animação'''
            if direita:
               
                self.image = pygame.transform.rotate(self.image, angle=-10)
                self.rect = self.image.get_rect(center=self.rect.center)
                self.rect.centerx = WIDTH/2
                self.rect.centery = HEIGHT - 50
            else:
                
                
                self.image = pygame.transform.rotate(self.image, angle=10)
                self.rect = self.image.get_rect(center=self.rect.center)
                self.rect.centerx = WIDTH/2
                self.rect.centery = HEIGHT - 50

    
        
       
            



class Alvo(pygame.sprite.Sprite):
        '''Classe para criar o alvo'''
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
    

class Altera_vel(pygame.sprite.Sprite):
        '''Classe para alterar a velocidade de lançamento dos projéteis que a estrela arremessa'''
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((20,200))
            self.image.fill(RED)
          
            self.rect = self.image.get_rect()
            self.rect.centerx = 10
            self.rect.centery = HEIGHT/2

            
            
          
            
        def update(self):
            '''Método para atualizar a posição dos pássaros e trocar as imagens dos pássaros para dar animação'''
            pass
    
class Planeta(pygame.sprite.Sprite):
        '''Classe para alterar a velocidade de lançamento dos projéteis que a estrela arremessa'''
        def __init__(self,raio, posicao):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((raio, raio))
            self.image.fill(RED)
          
            self.rect = self.image.get_rect()
            self.rect.centerx = posicao[0]
            self.rect.centery = posicao[1]

            
            
          
            
        def update(self):
            '''Método para atualizar a posição dos pássaros e trocar as imagens dos pássaros para dar animação'''
            pass
    