from imports import *

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