from imports import *
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