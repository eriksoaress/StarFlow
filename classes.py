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
            self.image = pygame.image.load("/home/fernando/Faculdade/3 semestre/Algelin. Teo. Info/aps0/jogo/StarFlow/estrela.png")
            self.image = pygame.transform.scale(self.image, (30,30))
            
            self.rect = self.image.get_rect()

            #Posição inicial da estrela
            self.rect.centerx = posicao_inicial_estrela[0]
            self.rect.centery = posicao_inicial_estrela[1]

            
            
          
            
        def update(self, velocidade ,atingiu):
            '''Método para atualizar a posição dos pássaros e trocar as imagens dos pássaros para dar animação'''

            # Se a estrela colidir com o alvo, ela volta para a posição inicial
            if atingiu:
                self.rect.centerx = posicao_inicial_estrela[0]
                self.rect.centery = posicao_inicial_estrela[1]

            # Se a estrela sair da tela, ela volta para a posição inicial
            if self.rect.centerx > 1310 or self.rect.centerx < -30 or self.rect.centery > 750 or self.rect.centery < -30:
                self.rect.centerx =posicao_inicial_estrela[0]
                self.rect.centery = posicao_inicial_estrela[1]

                return True
            # Nova posição da estrela
            self.rect.centerx = self.rect.centerx +  0.05*velocidade[0]
            self.rect.centery = self.rect.centery +  0.05*velocidade[1]
    
        
       
            



class Alvo(pygame.sprite.Sprite):
        '''Classe para criar o alvo'''
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("/home/fernando/Faculdade/3 semestre/Algelin. Teo. Info/aps0/jogo/StarFlow/Attack_2.png")
            self.image = pygame.transform.scale(self.image, (100,100))
          
            self.rect = self.image.get_rect()
            self.rect.center = np.array([1230,HEIGHT/2])

            
            
          
            
        def update(self):
            '''Método para atualizar a posição dos pássaros e trocar as imagens dos pássaros para dar animação'''
        
            self.rect.center = np.array([1230,random.randint(50, HEIGHT - 50) ])  
    
class Planeta(pygame.sprite.Sprite):
        '''Classe para alterar a velocidade de lançamento dos projéteis que a estrela arremessa'''
        def __init__(self,raio, posicao):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((raio, raio))
            self.image.fill(RED)

            self.rect = self.image.get_rect()
            self.rect.centerx = posicao[0]
            self.rect.centery = posicao[1]
           
 

            
                
          
            
        def update(self, estrela, velocidade_estrela, em_andamento):
            # Vetor que aponta da posição do planeta para a posição da estrela
            vetor = (np.array([estrela.rect.centerx, estrela.rect.centery ])- np.array([self.rect.centerx, self.rect.centery]))
            # gravidade  = 1000/(modulo_vetor**2)*vetor/modulo_vetor
            gravidade = (1000/(vetor[0]**2 + vetor[1]**2))*(vetor/(vetor[0]**2 + vetor[1]**2)**0.5)
   
            if em_andamento:
                # se a estrela tiver em movimento, a gravidade atua sobre ela, alterando sua posicao 
                estrela.rect.centerx = estrela.rect.centerx +  0.05*velocidade_estrela[0]
                estrela.rect.centery = estrela.rect.centery +  0.05*velocidade_estrela[1]
                # se a estrela tiver em movimento, a gravidade atua sobre ela, alterando sua velocidade
                velocidade_estrela[0] = velocidade_estrela[0] +  gravidade[0]
                velocidade_estrela[1] = velocidade_estrela[1] +  gravidade[1]

                


