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
            # Carrega a imagem da estrela e redimensiona para o tamanho desejado
            self.image = pygame.image.load(path / "imagens/estrela_padrao.png")
            self.image = pygame.transform.scale(self.image, (30,30))
            
            self.rect = self.image.get_rect()

            #Posição inicial da estrela
            self.rect.centerx = posicao_inicial_estrela[0]
            self.rect.centery = posicao_inicial_estrela[1]


        def update(self, velocidade ,atingiu, estrela=''):
            '''Método para atualizar a posição dos pássaros e trocar as imagens dos pássaros para dar animação'''
            if not estrela == '' :
                self.image = pygame.image.load(path / f"imagens/estrela_{estrela}.png")
                self.image = pygame.transform.scale(self.image, (30,30))
                # Definindo a posição
                self.rect = self.image.get_rect()
                self.rect.centerx = posicao_inicial_estrela[0]
                self.rect.centery = posicao_inicial_estrela[1]

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
            # Inicializa a classe pygame.sprite.Sprite
            pygame.sprite.Sprite.__init__(self)

            # Carrega a imagem do alvo e redimensiona para o tamanho desejado
            self.image = pygame.image.load(path / "imagens/Attack_2.png")
            self.image = pygame.transform.scale(self.image, (100,100))

            # Define a posição inicial do alvo
            self.rect = self.image.get_rect()
            self.rect.center = np.array([1230,HEIGHT/2])

                
        def update(self):
            '''Método para atualizar a posição do alvo e trocar sua imagem para criar animação'''

            # Atualiza a posição do alvo com uma posição aleatória na vertical
            self.rect.center = np.array([1230,random.randint(50, HEIGHT - 50) ])
    
class Planeta(pygame.sprite.Sprite):
        '''Classe para alterar a velocidade de lançamento dos projéteis que a estrela arremessa'''
        def __init__(self,raio, posicao):
            pygame.sprite.Sprite.__init__(self)

            # Carrega a imagem do planeta e ajusta seu tamanho
            self.image = pygame.image.load(path / f"imagens/planeta.png")
            self.image = pygame.transform.scale(self.image, (raio,raio))

            # Define a posição do planeta na tela
            self.rect = self.image.get_rect()
            self.rect.centerx = posicao[0]
            self.rect.centery = posicao[1]
            
        def update(self, state):
            # Calcula o vetor da estrela ao planeta e a direção da gravidade
            vetor_planeta_estrela = np.array([self.rect.centerx, self.rect.centery]) - np.array([state['estrela'].rect.centerx, state['estrela'].rect.centery])
            direcao_gravidade = vetor_planeta_estrela / np.linalg.norm(vetor_planeta_estrela)
            
            # Calcula a força gravitacional do planeta sobre a estrela
            DT = 100000/np.linalg.norm(vetor_planeta_estrela)**2
            gravidade = 0.2*DT * direcao_gravidade

            # Aplica a força gravitacional na velocidade da estrela
            if pygame.sprite.spritecollide(state['estrela'], state['poeiras'], False) :
                state['velocidade'] = state['velocidade']*0.99 +  gravidade
            else:
                state['velocidade'] = state['velocidade'] +  gravidade

            
             # Atualiza a posição da estrela de acordo com sua velocidade
            state['velocidade']  = state['velocidade'] +  gravidade
            state['estrela'].rect.centerx = state['estrela'].rect.centerx +  0.1*state['velocidade'][0]
            state['estrela'].rect.centery = state['estrela'].rect.centery +  0.1*state['velocidade'][1]
                    
            
            
           


class Poeira(pygame.sprite.Sprite):
        '''Classe para alterar as propriedades das poeiras'''
        def __init__(self,largura,altura, posicao):
            pygame.sprite.Sprite.__init__(self)
            # Carrega a imagem da poeira e ajusta o tamanho
            self.image = pygame.image.load(path / "imagens/poeira.png")
            self.image = pygame.transform.scale(self.image, (largura, altura))

            # Define a posição inicial da poeira
            self.rect = self.image.get_rect()
            self.rect.centerx = posicao[0]
            self.rect.centery = posicao[1]
            
        def update(self):
            # Define uma nova posição aleatória para a poeira
            self.rect.centery = self.rect.centery + 1
            #self.rect.center = np.array([random.randint(int(variaveis.raio_poeira/2), int(1280-variaveis.raio_poeira/2)), random.randint(int(variaveis.raio_poeira/2), int(720-variaveis.raio_poeira/2))])
            if self.rect.centery > 720:
                self.rect.centery = -30
                self.rect.centerx = random.randint(int(variaveis.raio_poeira/2) +400, int(1280-variaveis.raio_poeira/2))
            
class Tela_inicial(pygame.sprite.Sprite):
    '''Classe para criar a tela inicial'''

    def __init__(self):
        # Inicializa a superclasse
        pygame.sprite.Sprite.__init__(self)

        # Carrega a imagem de fundo
        self.image = pygame.image.load(path / 'imagens/wallpaper_estrelas.jpeg')

        # Obtém o retângulo que circunscreve a imagem
        self.rect = self.image.get_rect()

    



class Help(pygame.sprite.Sprite):
    '''
    Classe para criar a tela de ajuda, onde é explicado os níveis do jogo
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        # Carrega a imagem de fundo da tela de ajuda
        self.image = pygame.image.load(path / 'imagens/wallpaper_estrelas.jpeg')
        
        # Define o retângulo da imagem
        self.rect = self.image.get_rect()

class Asteroide(pygame.sprite.Sprite):
    '''Classe para criar os asteroides e movê-los em torno do planeta'''
    def __init__(self,raio, posicao, angle, increment):
        pygame.sprite.Sprite.__init__(self)
        # Carregando a imagem do asteroide e escalonando
        self.image = pygame.image.load(path / f'imagens/asteroide{random.randint(1,2)}.png')
        self.image = pygame.transform.scale(self.image, (raio,raio))
        # Definindo a posição do asteroide
        self.rect = self.image.get_rect()
        self.rect.centerx = posicao[0] + 200
        self.rect.centery = posicao[1] 
        self.angle = angle
        self.increment = increment

    def update(self, posicao):
        # Atualizando a posição do asteroide de acordo com o ângulo e a posição do planeta
        self.rect.centerx = posicao[0]  + 100*math.cos(math.radians(self.angle)) 
        self.rect.centery = posicao[1] + 100*math.sin(math.radians(self.angle))
        self.angle = self.angle + self.increment
        

class Vida(pygame.sprite.Sprite):
    '''Classe para criar os corações que representam as vidas do jogador'''
    def __init__(self,num):
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem do coração e escalonando
        self.image = pygame.image.load(path / f'imagens/vida{num}.png')
        self.image = pygame.transform.scale(self.image, (250,200))
        # Definindo a posição do coração
        self.rect = self.image.get_rect()
        self.rect.centerx = 120
        self.rect.centery = 50
    def update(self,num):
        self.image = pygame.image.load(path / f'imagens/vida{num}.png')
        self.image = pygame.transform.scale(self.image, (250,200))
        # Definindo a posição do coração
        self.rect = self.image.get_rect()
        self.rect.centerx = 120
        self.rect.centery = 50
    
class Game_over(pygame.sprite.Sprite):
    '''Classe para criar a tela de game over'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo da tela de game over
        self.image =pygame.Surface((1280,720))
        self.image.fill((0,0,0))
        self.image.set_alpha(200)

        
        # Definindo o retângulo da imagem
        self.rect = self.image.get_rect()
        self.rect.centerx = 640
        self.rect.centery = 360

