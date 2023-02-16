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
            self.image = pygame.image.load("StarFlow/estrela.png")
            self.image = pygame.transform.scale(self.image, (50,50))
            
        
           
           
          
            self.rect = self.image.get_rect()
            self.rect.centerx = 50
            self.rect.centery = HEIGHT/2

            
            
          
            
        def update(self, velocidade):
            '''Método para atualizar a posição dos pássaros e trocar as imagens dos pássaros para dar animação'''
    
            # if direita:
               
            #     self.image = pygame.transform.rotate(self.image, angle=-10)
            #     self.rect = self.image.get_rect(center=self.rect.center)
            #     self.rect.centerx = WIDTH/2
            #     self.rect.centery = HEIGHT - 50
            # else:
                
                
            #     self.image = pygame.transform.rotate(self.image, angle=10)
            #     self.rect = self.image.get_rect(center=self.rect.center)
            #     self.rect.centerx = WIDTH/2
            #     self.rect.centery = HEIGHT - 50
            if velocidade[0] < 1 and  velocidade[0] > 0 :
                self.rect.centerx += 1
            self.rect.centerx += velocidade[0]
            self.rect.centery -= velocidade[1]

    
        
       
            



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
            self.image = pygame.Surface((400,50))
            self.image.fill(RED)
          
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH/2
            self.rect.centery = 695

 
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
    
class Mira1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill(RED)
      
        self.rect = self.image.get_rect()
        self.rect.centerx = 90
        self.rect.centery = HEIGHT/2
    
    def update(self, direita):
        if direita == 2:
            self.rect.centery += 2
        elif direita == 3:
            self.rect.centery -= 2
        

class Mira2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,30))
        self.image.fill(RED)
      
        self.rect = self.image.get_rect()
        self.rect.centerx = 78 
        self.rect.centery = HEIGHT/2
    
    def update(self, direita):
        if direita == 2:
            self.rect.centery += 1
        elif direita == 3:
            self.rect.centery -= 1