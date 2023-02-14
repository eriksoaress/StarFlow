import json
import pygame
import variaveis
import random
from constantes import*



   



class Estrela(pygame.sprite.Sprite):
        '''Classe para criar pássaros'''
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(pygame.image.load("imagem/passaros.png"),[120,90])
            
        def update(self):
            '''Método para atualizar a posição dos pássaros e trocar as imagens dos pássaros para dar animação'''
            pass
