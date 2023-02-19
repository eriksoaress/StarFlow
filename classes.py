import json
import pygame
import variaveis
import random
from constantes import*
import numpy as np

SURFACE_COLOR = (167, 255, 100)



    

class Estrela(pygame.sprite.Sprite):
        '''Classe para criar a estrela, o objeto que disparará no alvo'''
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("estrela.png")
            self.image = pygame.transform.scale(self.image, (30,30))
            
            self.rect = self.image.get_rect()

            #Posição inicial da estrela
            self.rect.center = posicao_inicial_estrela

            
            
          
            
        def update(self, velocidade ,atingiu):
            '''Método para atualizar a posição dos pássaros e trocar as imagens dos pássaros para dar animação'''

            # Se a estrela colidir com o alvo, ela volta para a posição inicial
            if atingiu:
                self.rect.center = posicao_inicial_estrela

            # Se a estrela sair da tela, ela volta para a posição inicial
            if self.rect.center[0] > 1310 or self.rect.center[0] < -30 or self.rect.center[1] > 750 or self.rect.center[1] < -30:
                self.rect.center =posicao_inicial_estrela
                return True
            # Nova posição da estrela
            self.rect.center = self.rect.center +  0.05*velocidade
    
        
       
            



class Alvo(pygame.sprite.Sprite):
        '''Classe para criar o alvo'''
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("Attack_2.png")
            self.image = pygame.transform.scale(self.image, (100,100))
          
            self.rect = self.image.get_rect()
            self.rect.center = np.array([1230,HEIGHT/2])

            
            
          
            
        def update(self):
            '''Método para atualizar a posição dos pássaros e trocar as imagens dos pássaros para dar animação'''
        
            self.rect.center = np.array([1230,random.randint(50, HEIGHT - 50) ])  
    
class Planeta(pygame.sprite.Sprite):
        '''Classe para alterar a velocidade de lançamento dos projéteis que a estrela arremessa'''
        def __init__(self,raio, posicao, em_andamento):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((raio, raio))
            self.image.fill(RED)

            self.rect = self.image.get_rect()
            self.rect.center = posicao
            self.em_andamento = em_andamento
        @classmethod
        def calcula_modulo(vetor):
            return (vetor[0]**2 + vetor[1]**2)**(1/2)
        @classmethod
        def vetor_unitario(vetor):
            return vetor/(vetor[0]**2 + vetor[1]**2)**(1/2)

            
            
          
            
        def update(self, estrela, velocidade_estrela):
            '''Método para atualizar a posição dos pássaros e trocar as imagens dos pássaros para dar animação'''
            vetor = (np.array(estrela.rect.center)- np.array(self.rect.center))
            gravidade = (1000/((vetor[0]**2 + vetor[1]**2)**(1/2))**2)*vetor/(vetor[0]**2 + vetor[1]**2)**(1/2)
            if self.em_andamento:
                velocidade_estrela += gravidade
                


    
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