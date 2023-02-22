import json
import pygame
import variaveis
import random
from constantes import*
import numpy as np
import math
SURFACE_COLOR = (167, 255, 100)

class Estrela(pygame.sprite.Sprite):
        '''Classe para criar a estrela, o objeto que disparará no alvo'''
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(path / "imagens/estrela.png")
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
           

class Alvo(pygame.sprite.Sprite):
        '''Classe para criar o alvo'''
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(path / "imagens/Attack_2.png")
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
            self.image = pygame.image.load(path / f"imagens/planeta.png")
            self.image = pygame.transform.scale(self.image, (raio,raio))

            self.rect = self.image.get_rect()
            self.rect.centerx = posicao[0]
            self.rect.centery = posicao[1]
    
        def update(self, state):
            vetor_planeta_estrela = np.array([self.rect.centerx, self.rect.centery]) - np.array([state['estrela'].rect.centerx, state['estrela'].rect.centery])
            direcao_gravidade = vetor_planeta_estrela / np.linalg.norm(vetor_planeta_estrela)
            DT = 100000/np.linalg.norm(vetor_planeta_estrela)**2
            gravidade = 0.3*DT * direcao_gravidade

            if pygame.sprite.spritecollide(state['estrela'], state['poeiras'], False) :
                state['velocidade'] = state['velocidade']*0.99 +  gravidade
            else:
                state['velocidade']  = state['velocidade'] +  gravidade
            
            
            state['velocidade']  = state['velocidade'] +  gravidade
            state['estrela'].rect.centerx = state['estrela'].rect.centerx +  0.1*state['velocidade'][0]
            state['estrela'].rect.centery = state['estrela'].rect.centery +  0.1*state['velocidade'][1]
   

class Poeira(pygame.sprite.Sprite):
        '''Classe para alterar as propriedades das poeiras'''
        def __init__(self,largura,altura, posicao):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(path / "imagens/poeira.png")
            self.image = pygame.transform.scale(self.image, (largura,altura))

            self.rect = self.image.get_rect()
            self.rect.centerx = posicao[0]
            self.rect.centery = posicao[1]
           
 

            
        def update(self):
            pass
         

                
    

class Tela_inicial(pygame.sprite.Sprite):
    '''Classe para criar a tela inicial'''
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(path / 'imagens/wallpaper_estrelas.jpeg')
            self.rect = self.image.get_rect()
    




class Help(pygame.sprite.Sprite):
    '''Classe para criar a tela de ajuda, onde fica explicado os níveis do jogo'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path / 'imagens/wallpaper_estrelas.jpeg')
        self.rect = self.image.get_rect()

class Asteroide(pygame.sprite.Sprite):
    def __init__(self, posicao):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5,5))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = posicao[0] + 200
        self.rect.centery = posicao[1] 

    def update(self, posicao, angle):
        
        self.rect.centerx = posicao[0]  + 100*math.cos(math.radians(angle)) 
        self.rect.centery = posicao[1] + 100*math.sin(math.radians(angle))
        